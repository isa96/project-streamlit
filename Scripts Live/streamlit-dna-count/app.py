import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

st.image(Image.open('dna.jpg'), use_column_width=True)

"""
# DNA Nucleotide Counter
Made with **streamlit** 
***
"""

seq = st.text_input('Insert a DNA Sequence')
"""
Your input
"""
seq
"Input length "
st.text(len(seq))

A_count = seq.count('A')
T_count = seq.count('T')
G_count = seq.count('G')
C_count = seq.count('C')

dna_count = {'Nucleotide':['Adenine', 'Thymine', 'Guanine', 'Cytosine'], 'Count':[A_count, T_count, G_count, C_count]}
df = pd.DataFrame(dna_count)

fig = px.bar(df, x='Nucleotide', y='Count', color='Nucleotide')
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)