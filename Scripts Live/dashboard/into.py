import streamlit as st
import lorem
from numerize import numerize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout="wide")

st.write("Hello World!")

"Ini hello world, tapi pake magic"

st.title("Ini Judul")
st.subheader("Ini subheader")
st.write(lorem.paragraph())

st.code("import streamlit as st")
st.text(lorem.paragraph())

# Deklarasi dataset
df = pd.read_csv("store.csv")

# Data prep
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# End of Data Prep

st.dataframe(df)

# metrics
st.metric("Total Sales", 1000, 10)

st.metric("Total Profit", "$ 10M", "-2.3%")

st.title("Charting")

# Sidebar

with st.sidebar:
    st.title("Dashboard store")
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))
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

# Line chart (Sales)

sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()

cap1, cht1 = st.columns([1, 4])
with cap1:
    st.dataframe(sales)

with cht1:
    st.line_chart(sales)

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
    "Pilih jurusan Kamu",
    ('Matematika', 'Fisika', 'Kimia')
)
st.write("Kamu memilih jurusan ", jurusan)

setuju = st.checkbox("Centang untuk setuju")
if setuju:
    st.write("Anda sudah setuju")
else:
    st.write("Anda belum setuju")

nama = st.text_input("Masukkan nama kamu")
st.write("Hello ", nama)

# Image
image = Image.open("meme-python.png")
st.image(image, caption = "Ini meme")

#Penggunaan Kolom
st.title("Kolom")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(lorem.paragraph())

with col2:
    st.write(lorem.paragraph())

with col3:
    st.write(lorem.paragraph())

angka = st.number_input("Masukkan angka", 0)
if angka % 2 == 0:
    st.success("Angka genap")
else:
    st.error("Angka ganjil")