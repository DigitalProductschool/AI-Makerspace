import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
from transformers import pipeline
import os
import openai

# Add this line to configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


load_dotenv()

# Create zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define emotion labels
emotion_labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion',
                  'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment',
                  'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism',
                  'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']

# Define other labels
hatespeech_labels = ["Acceptable", "Inappropriate", "Offensive", "Violent"]
sexism_labels = ["Sexist", "Not Sexist"]

st.set_page_config(
    page_title="GoEmotions Dashboard",
    layout="wide"
)

# Set page title
st.title("GoEmotions Dashboard - Analyzing Emotions in Text")


# Define color map for each emotion category
color_map = {
    'admiration': ['#1f77b4', '#98df8a', '#2ca02c', '#d62728'],
    'amusement': ['#ff7f0e', '#98df8a', '#2ca02c', '#d62728'],
    'anger': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'annoyance': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'approval': ['#1f77b4', '#98df8a', '#2ca02c', '#d62728'],
    'caring': ['#98df8a', '#2ca02c', '#FF69B4', '#d62728'],
    'confusion': ['#ffbb78', '#ff7f0e', '#9467bd', '#d62728'],
    'curiosity': ['#ffbb78', '#ff7f0e', '#9467bd', '#d62728'],
    'desire': ['#2ca02c', '#ff7f0e', '#98df8a', '#d62728'],
    'disappointment': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'disapproval': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'disgust': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'embarrassment': ['#ffbb78', '#ff7f0e', '#9467bd', '#d62728'],
    'excitement': ['#ff7f0e', '#2ca02c', '#98df8a', '#d62728'],
    'fear': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'gratitude': ['#98df8a', '#2ca02c', '#1f77b4', '#d62728'],
    'grief': ['#ffbb78', '#d62728', '#bcbd22', '#ff7f0e'],
    'joy': ['#ff7f0e', '#98df8a', '#2ca02c', '#d62728'],
    'love': ['#FF69B4', '#98df8a', '#2ca02c', '#d62728'],
    'nervousness': ['#ffbb78', '#ff7f0e', '#9467bd', '#d62728'],
    'optimism': ['#98df8a', '#2ca02c', '#1f77b4', '#d62728'],
    'pride': ['#98df8a', '#ff7f0e', '#1f77b4', '#d62728'],
    'realization': ['#9467bd', '#ff7f0e', '#ffbb78', '#d62728'],
    'relief': ['#1f77b4', '#98df8a', '#2ca02c', '#d62728'],
    'remorse': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'sadness': ['#ffbb78', '#ff7f0e', '#d62728', '#bcbd22'],
    'surprise': ['#ff7f0e', '#ffbb78', '#9467bd', '#d62728'],
    'neutral': ['#2ca02c', '#98df8a', '#1f77b4', '#d62728']
}

default_options = [
    "I'm so excited for my vacation next week!",
    "I'm feeling so stressed about work.",
    "I just received great news from my doctor!",
    "I can't wait to see my best friend tomorrow.",
    "I'm feeling so lonely and sad today."
    "I'm so angry at my neighbor for being so rude.",
    "You are so annoying!",
    "You people from small towns are so dumb.",
    "If you don't agree with me, you are a moron.",
    "I hate you so much!",
    "If you don't listen to me, I'll beat you up!",
]

def suggest_alternative_text(original_text, label):
    prompt = f"""The following sentence: '{original_text}' has been flagged as '{label}'.
                To align with responsible communication guidelines, a more appropriate phrasing could be:"""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Concatenate the prompt and the generated text to form a complete message
    complete_message = f"{prompt}\n{response.choices[0].text.strip()}"
    return complete_message


with st.sidebar:
    # Create dropdown with default options
    selected_option = st.selectbox("Select a default option or enter your own text:", default_options)

    # Display text input with selected option as default value
    text_input = st.text_area("Enter text to analyze emotions:", value=selected_option, height=100)

    # Add submit button
    submit = st.button("Submit")

# If submit button is clicked
if submit:
    # Call API and get predicted probabilities for each emotion category and hate speech classification
    payload = {"inputs": text_input, "options": {"wait_for_model": True, "use_cache": True}}

    # Obtain predictions from classifier
    predicted_probabilities_ED = classifier(text_input, emotion_labels, multi_label=True)
    predicted_probabilities_HS = classifier(text_input, hatespeech_labels)
    predicted_probabilities_SD = classifier(text_input, sexism_labels)


    # Extract labels and scores
    labels = predicted_probabilities_ED['labels']
    scores = predicted_probabilities_ED['scores']

    # Zip the labels and scores together and sort by scores in descending order
    sorted_emotions = sorted(zip(labels, scores), key=lambda x: x[1], reverse=True)

    # Take the top 4
    top_emotions = sorted_emotions[:4]
    # get the predicted label for hate speech
    hate_detection = predicted_probabilities_HS['labels'][0]
    sexism_detection = predicted_probabilities_SD['labels'][0]

    #detected_labels = [label for label, score in top_emotions]
    #detected_labels.append(hate_detection)
    #detected_labels.append(sexism_detection)


    # Creating columns to visualize the results 
    ED, _, HS, __, SD = st.columns([4,1,2,1,2])


    negative_emotion_labels = set(['anger', 'annoyance', 'disappointment', 'disapproval', 'disgust', 
                               'embarrassment', 'fear', 'grief', 'nervousness', 'remorse', 'sadness'])
    negative_hatespeech_labels = set(['Inappropriate', 'Offensive', 'Violent'])
    negative_sexism_labels = set(['Sexist'])

    detected_labels = [label for label, score in top_emotions]
    detected_labels.append(hate_detection)
    detected_labels.append(sexism_detection)


    negative_detected_labels = list(filter(lambda label: label in negative_emotion_labels or label in negative_hatespeech_labels or label in negative_sexism_labels, detected_labels))

    




    with ED:
        # Create the gauge charts for the top 4 emotion categories
        fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'indicator'}, {'type': 'indicator'}],
                                                [{'type': 'indicator'}, {'type': 'indicator'}]],
                            vertical_spacing=0.4)

    for i, emotion in enumerate(top_emotions):
        # Get the emotion category, color, and normalized score for the current emotion
        category, value = emotion
        color = color_map[category]
        value *= 100  # normalize the score to percentage
            
        # Calculate the row and column position for adding the trace to the subplots
        row = i // 2 + 1
        col = i % 2 + 1

                
        # Add a gauge chart trace for the current emotion category
        fig.add_trace(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=value,
            mode="gauge+number",
            title={'text': category.capitalize()},
            gauge={'axis': {'range': [None, 100]},
                'bar': {'color': color[3]},
                'bgcolor': 'white',
                'borderwidth': 2,
                'bordercolor': color[1],
                'steps': [{'range': [0, 33], 'color': color[0]},
                            {'range': [33, 66], 'color': color[1]},
                            {'range': [66, 100], 'color': color[2]}],
                'threshold': {'line': {'color': "black", 'width': 4},
                                'thickness': 0.5,
                                'value': 50}}), row=row, col=col)

        # Update the layout of the figure
        fig.update_layout(height=400, margin=dict(t=50, b=5, l=0, r=0))


    # Display gauge charts
    st.text("")
    st.text("")
    st.text("")
    st.subheader("Emotion Detection")
    st.text("")
    st.plotly_chart(fig, use_container_width=True)
    
    with _:
        st.text("")
        

    with HS:
        # Display Hate Speech Classification
        #hate_detection = predicted_probabilities_HS['labels'][0]
        st.text("")
        st.text("")
        st.text("")
        st.subheader("Hate Speech Analysis")
        st.text("")
        st.image(f"assets/{hate_detection}.jpg", width=200)
        st.text("")
        st.text("")
        st.markdown(f"#### The given text is: {hate_detection}")

    with __:
        st.text("")

    with SD:
        #sexism_detection = predicted_probabilities_SD['labels'][0]
        st.text("")
        st.text("")
        st.text("")
        st.subheader("Sexism Detection")
        st.text("")
        st.image(f"assets/{sexism_detection}.jpg", width=200)
        st.text("")
        st.text("")
        st.markdown(f"#### The given text is: {sexism_detection}")

    # Check if any negative label is detected
    if negative_detected_labels:
        # Let's use the first detected negative label
        negative_label = negative_detected_labels[0]
    
        # Call the OpenAI API to suggest an alternative text
        alternative_text = suggest_alternative_text(text_input, negative_label)

        # Display the alternative text to the user
        st.subheader("Suggested Alternative Text")
        st.write(alternative_text)

        

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)