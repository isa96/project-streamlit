import streamlit as st
# pip install lorem
import lorem
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from numerize import numerize

st.set_page_config(layout="wide")

st.write("Hello World!")

"Ini hello world, tapi make magic"

st.title("Ini Judul")
st.subheader("Ini subheader")

st.write(lorem.paragraph())

st.code("import streamlit as st")
st.text(lorem.paragraph())

# deklare dataset
df = pd.read_csv("store.csv")

# change to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# show dataframe
st.dataframe(df)


# metrics
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric("Total Sales", 1000, 10)
st.metric("Total Profit", "$ 10M", "-2.3%")

st.title("Charting")


# LINE CHART SALES
# per Month
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample('M').sum()

st.line_chart(
    sales
)

# per week
sales2 = df[['Order Date', 'Sales']].set_index('Order Date').resample('W').sum()

st.line_chart(
    sales2
)



# FROM SEABORN

fig1, ax1 = plt.subplots(figsize=(10,10))
sns.scatterplot(
    data=df,
    x='Sales',
    y='Profit',
    ax = ax1
)
st.pyplot(fig1)

# Input
st.title("Input")

tombol1 = st.button("Tekan tombol ini")
st.write(tombol1)


jurusan = st.selectbox(
    "Pilih jurusan kamu",
    ("Matematika", "Fisika", "Kimia")
)
st.write("kamu memilih jurusan", jurusan)



setuju = st.checkbox("Centang untuk setuju")

if setuju:
    st.write("Anda sudah setuju")
else:
    st.write("Anda belum setuju")



nama = st.text_input("Masukkan nama kamu")
st.write("Hello", nama)



# Image
image = Image.open("imam.jpg")
st.image(image, caption="Ini Avatarkuuuu")



# Column
st.title("Kolom")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(lorem.paragraph())

with col2:
    st.write(lorem.paragraph())

with col3:
    st.write(lorem.paragraph())

st.markdown("---")

# size kontribusi column
# anggap 5 size
# 1 caption
# 4 linechart
cap1, cht1 = st.columns([1, 4])
with cap1:
    st.write(lorem.paragraph())
with cht1:
    st.line_chart(
        sales
    )

st.markdown("---")

df_sales, cht2 = st.columns([1, 4])
with df_sales:
    st.dataframe(sales)
with cht2:
    st.line_chart(
        sales
    )




st.markdown("---")

st.title("Charting")

# Sidebar
with st.sidebar:
    st.title("Dashboard store")

# Metrics 
met1, met2, met3 = st.columns(3)
with met1:
    st.metric(
        "Total Sales", 
        "$ " + numerize.numerize(df['Sales'].sum()),
        "3.4%"
    )

with met2:
    st.metric("Total Order", df['Order ID'].nunique())

with met3:
    st.metric("Number of Customers", df['Customer ID'].nunique())

# Input Frequensi
freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()

df_sales, cht2 = st.columns([1, 4])
with df_sales:
    st.dataframe(sales)
with cht2:
    st.line_chart(
        sales
    )









st.markdown("---")

st.title("Charting with Sidebar")

# Sidebar
with st.sidebar:
    st.title("Dashboard store")
    # Input Frequensi
    freq2 = st.selectbox("Masukkan frekuensinya", ('D', 'W', 'M', 'Q', 'Y'))
    with st.expander("Ketahui lebih lanjut..."):
        st.write(lorem.paragraph())


# Metrics 
met1, met2, met3 = st.columns(3)

with met1:
    st.metric(
        "Total Sales", 
        "$ " + numerize.numerize(df['Sales'].sum()),
        "3.4%"
    )

with met2:
    st.metric("Total Order", df['Order ID'].nunique())

with met3:
    st.metric("Number of Customers", df['Customer ID'].nunique())


sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq2).sum()
df_sales, cht2 = st.columns([1, 4])
with df_sales:
    st.dataframe(sales)
with cht2:
    st.line_chart(
        sales
    )


st.markdown("---")


angka = st.number_input("Masukkan angka", 0)

if angka % 2 == 0:
    st.success("Angka genap")
else:
    st.error("Angka ganjil")


df