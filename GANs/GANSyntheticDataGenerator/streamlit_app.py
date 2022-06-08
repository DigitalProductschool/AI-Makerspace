import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from sdv.tabular import CTGAN
import pandas as pd
import streamlit as st

st.set_page_config()
# st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Tabular Data Generator")
st.text("The solution uses Conditional GANS to generate synthetic data")

# file(s) part
dataframe=None
uploaded_file = st.file_uploader("Choose your CSV file")
if uploaded_file is not None:
  dataframe = pd.read_csv(uploaded_file)

Primary_Key = st.sidebar.text_input('Enter Primary Column Name')
if not Primary_Key:
  Primary_Key=None

# sidebar parameters part
No_of_samples = st.sidebar.number_input('Enter Number of Rows to Generate',value = 200)

# model_name = st.sidebar.text_input("Enter your Model Name")

# model part
#@st.cache(allow_output_mutation=True)
def data_generator():
  model = CTGAN(primary_key=Primary_Key)
  model.fit(dataframe)
  return model.sample(num_rows=No_of_samples) # put it above and return model

# def load_model():
#   model = CTGAN.load(model_file_name)
#   return model

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# model_file_name = "{}.pkl".format(model_name)

if st.button('Generate'):
  if dataframe is None:
    st.error("Please Upload Your CSV")
  else:
    with st.spinner('Abra ka dabra...'):
    # mymodel = create_model()

    # mymodel.save("{}.pkl".format(model_name))

    # st.download_button(label="Download Model file", file_name=model_file_name, data=model_file_name)
    
    # with st.spinner('Loading Model Into Memory....'):
    #   model = load_model()
    #   new_data = model.sample(num_rows=No_of_samples)
      new_data = data_generator()
      csv = convert_df(new_data)
      st.download_button(label="Download Generated Output CSV", file_name='synthetic_data.csv', data=csv, mime='text/csv')
      st.success('And your file is ready!')