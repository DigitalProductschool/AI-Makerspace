
import streamlit as st
from llama_index.core import(
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
    Document,
    get_response_synthesizer,
    StorageContext
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.langchain_helpers.agents import IndexToolConfig, LlamaIndexTool
#from llama_index.ingestion import IngestionPipeline
#from llama_index.text_splitter import SentenceSplitter
#from llama_index.extractors import (
 #   TitleExtractor,
 #   QuestionsAnsweredExtractor,
 #   SummaryExtractor,
 #   KeywordExtractor,
 #   EntityExtractor
#)
#from llama_index.schema import MetadataMode
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.postprocessor.cohere_rerank import CohereRerank
import qdrant_client
from langchain.memory import ConversationBufferMemory
import time
import nest_asyncio
from dotenv import load_dotenv
import tempfile
import os

nest_asyncio.apply()
#import openai

load_dotenv()

llm=OpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2
    )
embed_model = OpenAIEmbedding()

client = qdrant_client.QdrantClient(location=":memory:")
vector_store = QdrantVectorStore(client=client, collection_name="test_store")

storage_context = StorageContext.from_defaults(vector_store=vector_store)

cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_rerank = CohereRerank(api_key=cohere_api_key, top_n=2)

# Set the header of the Streamlit application
st.header("Workshop Transcript Chatbot")

# Initialize session state to store the chat history
if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about DPS Workshops!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data(uploaded_files):
    """
    Load and index workshop transcripts uploaded by the user.

    Args:
        uploaded_files: A list of uploaded file objects.

    Returns:
        VectorStoreIndex: An indexed representation of the workshop transcripts.
    """
    with st.spinner(text="Indexing uploaded workshop docs – hang tight! This might take some time."):
        with tempfile.TemporaryDirectory() as temp_dir:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    file_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

            reader = SimpleDirectoryReader(input_dir=temp_dir, recursive=True)
            docs = reader.load_data()

            if docs:
                service_context_for_indexing = ServiceContext.from_defaults(embed_model = embed_model)
                # Execute pipeline and time the process
                index =  VectorStoreIndex.from_documents(docs,storage_context=storage_context)

                return index
            else:
                return None

# Streamlit file uploader
uploaded_files = st.file_uploader("Upload workshop documents", accept_multiple_files=True)

if uploaded_files:
    index = load_data(uploaded_files)

    if index:
        # Set up the ServiceContext with the LLM for the querying stage
        service_context_for_querying = ServiceContext.from_defaults(
            llm=llm,
            embed_model=embed_model
            )

        # configure retriever
        retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=5,
        )

        # configure response synthesizer
        response_synthesizer = get_response_synthesizer(
            response_mode="tree_summarize",
        )

        # assemble query engine
        query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            node_postprocessors=[cohere_rerank])


        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True
            )


        tool_config = IndexToolConfig(
            query_engine=query_engine,
            name=f"Vector Index",
            description=f"useful for when you want to answer queries about the document",
            tool_kwargs={"return_direct": True},
            memory = memory
            )

        # create the tool
        tool = LlamaIndexTool.from_tool_config(tool_config)

        # Chat interface for user input and displaying chat history
        if prompt := st.chat_input("Your question"):
            st.session_state.messages.append({"role": "user", "content": prompt})
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Generate and display the response from the chat engine
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Retrieve the response from the chat engine based on the user's prompt
                    response=tool.run(prompt)
                    #st.write(response.response)
                    st.write(response)
                    #message = {"role": "assistant", "content": response.response}
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message) # Add response to message history
