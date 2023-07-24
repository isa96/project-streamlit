import streamlit as st
import pandas as pd
import base64
import numpy as np
import plotly.express as px

st.set_page_config(page_title="NBA Player Stats Explorer", layout="wide")

'''
# NBA Player Stats Explorer
Made with **streamlit** 
***
'''

st.sidebar.header('Filter')
year = st.sidebar.selectbox('Year', list(reversed(range(1950,2022))))

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df['Age']=='Age'].index)
    raw.fillna(0, inplace=True)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(year)

team_list = sorted(playerstats['Tm'].unique())
selected_team = st.sidebar.multiselect('Team', team_list, team_list)

pos_list = sorted(playerstats['Pos'].unique())
selected_pos = st.sidebar.multiselect('Position', pos_list, pos_list)

df = playerstats[(playerstats['Tm'].isin(selected_team)) & (playerstats['Pos'].isin(selected_pos))].reset_index(drop=True)
st.dataframe(df)

col1, col2 = st.beta_columns(2)

with col1:
    st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')

with col2:
    st.markdown("<p style='text-align: right;'>" + filedownload(df) + "</p>", unsafe_allow_html=True)