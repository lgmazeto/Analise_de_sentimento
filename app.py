import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns
from PIL import Image


image = Image.open('Presidenciaveis_2022.jpeg')
st.image(image)
st.title('Presidenciaveis 2022')

df = pd.read_csv('Conjunto de Dados/df_presidenciaveis_sentimentos.csv')
candidato = df['Candidato'].unique()
select_candidato = st.sidebar.multiselect('Candidato',candidato, candidato)

df_select_candidato = df[(df['Candidato'].isin(select_candidato))]
df_grafico = df_select_candidato[['Sentimento']]
sns.set(rc = {'figure.figsize':(10,8)})

st.dataframe(df_select_candidato[['Data','Tweet','Sentimento']])
st.bar_chart(df_grafico, use_container_width=True)
