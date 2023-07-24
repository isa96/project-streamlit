import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Iris Flower Classification", layout="wide")

st.write("""
# Simple Iris Flower Prediction App
Made with **streamlit** 
""")

st.sidebar.header('Set Features')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
iris_df = pd.DataFrame(data = np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
iris_df['target'].replace({0.0:'setosa', 1.0:'versicolor', 2.0:'virginica'}, inplace=True)

fig1 = px.scatter(data_frame=iris_df, x='sepal length (cm)', y='sepal width (cm)', color='target', template='plotly_dark')
fig1.add_trace(go.Scatter(x=df['sepal_length'], y=df['sepal_width'], name='user input', mode='markers', marker_symbol='x', marker_size=15))

fig2 = px.scatter(data_frame=iris_df, x='petal length (cm)', y='petal width (cm)', color='target', template='plotly_dark')
fig2.add_trace(go.Scatter(x=df['petal_length'], y=df['petal_width'], name='user input', mode='markers', marker_symbol='x', marker_size=15))

col1, col2 = st.beta_columns(2)
with col1:
    st.header("Sepal Characteristics")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.header("Petal Characteristics")
    st.plotly_chart(fig2, use_container_width=True)

X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction Probability')
pp = pd.DataFrame(data=prediction_proba, columns=['setosa', 'versicolor', 'virginica'])
st.write(pp)