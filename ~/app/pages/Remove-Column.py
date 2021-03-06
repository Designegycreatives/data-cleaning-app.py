import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
from PIL import Image 

col1, col2 = st.columns(2)
image = Image.open('gif.gif')


col1.header("Split Your Data Into Columns")
col1.write("This makes your data looks organized")
col2.image(image)


df_file = st.file_uploader("Upload your file: ", type=['csv', 'xlsx', 'pickle'])
try:
  df_file = pd.read_csv(df_file)
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  st.write("Upload A CSV, EXCEL OR PICKLE FILE")

# Open Excel File
try:
  df_file = pd.read_excel(df_file, engine='openpyxl')
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  pass

# Read Pickle File
try:
  df_file = pd.read_pickle(df_file)
  st.markdown("Your Data Record: ")
  st.dataframe(df_file)
except:
  pass

try:
   col_del = st.multiselect("Choose Column:",options=df_file.columns)
   coldel = df_file.drop(columns=col_del, axis=1, inplace=True)
   if st.button('New Data'):
     st.write(df_file)
   
     coldel = pd.DataFrame(df_file)
     file_name = "clean_data.csv"
     file_path = f"./{file_name}"

     df_file.to_csv(file_path)

     df_file= open(file_path, 'rb')
     st.download_button(label='Click to download',
                      data=df_file,
                      file_name=file_name,
                      key='download_df_clean')
     df_file.close()
except:
  pass
