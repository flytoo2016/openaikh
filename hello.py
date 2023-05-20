import pandas as pd
from pandasai import PandasAI
import streamlit as st
# Instantiate a LLM
from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token="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")
st.title('PandasAI')
st.header('pandaAi APP is a conversational AI for pandas')
file = st.file_uploader("Upload file", type=["csv", "txt"])
question = st.text_input('Question', 'Which are the 5 happiest countries?')
# create dataframe from the file uploaded
if file is not None:
    df= pd.read_csv(file)
    st.write(df)
if st.button("ASK") and (file is not None) and (question is not None):
    pandas_ai = PandasAI(llm, conversational=False)
    # add spinner 
    with st.spinner('Wait for it...'):
        xyz= pandas_ai(df, prompt=question)
        st.write(xyz)
#df = pd.DataFrame({ #   "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
  #  "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
   # "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
#})

