import streamlit as st
import pandas as pd
import numpy as np
from numerize import numerize

st.set_page_config(layout="wide")

df = pd.read_csv('store.csv')

# Data preprocessing

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# *** End of data preprocessing *** 

with st.sidebar:
    st.title("Store Dashboard")
    freq = st.selectbox(
        "Select frequency",
        ('D', 'W' , 'M', 'Q', 'Y'))
    year = st.selectbox(
        "Select year",
        sorted(df['Order Date'].dt.year.unique())
    )

met1, met2, met3 = st.columns(3)
with met1:
    df_now = df[(df['Order Date'].dt.year == year) & (df['Ship Date'].dt.year == year)]
    df_last = df[(df['Order Date'].dt.year == year-1) & (df['Ship Date'].dt.year == year-1)]

    sales_delta = (df_now['Sales'].sum() - df_last['Sales'].sum()) / df_last['Sales'].sum()

    st.metric(
        "Total sales",
        numerize.numerize(df_now['Sales'].sum()),
        str(round(sales_delta*100,2)) + "%"
        )
with met2:
    st.metric("Total transaction",df['Order ID'].nunique())
with met3:
    st.metric("Number of customers",df['Customer ID'].nunique())

st.subheader("Sales")
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()
st.line_chart(
    sales
)

cust_seg_bar, sales_seg = st.columns(2)
with cust_seg_bar:
    st.subheader("Customer Segment")
    st.bar_chart(
        df.groupby('Segment').nunique()['Customer ID']
    )

with sales_seg:
    sales_by_seg = pd.pivot_table(
        data=df,
        index='Order Date',
        columns='Segment',
        values='Sales',
        aggfunc='sum'
    ).resample(freq).sum()

    st.subheader("Sales by Segment")
    st.line_chart(
    pd.DataFrame(
        data = sales_by_seg.values,
        index = sales_by_seg.index,
        columns = list(sales_by_seg.columns)
        )
    )

st.subheader("Year "+ str(year) +" Transaction")
st.dataframe(df_now)

st.subheader("Year "+ str(year-1) +" Transaction")
st.dataframe(df_last)