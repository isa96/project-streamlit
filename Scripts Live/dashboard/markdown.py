import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import lorem
from PIL import Image

# Dashboard setup
st.set_page_config(layout="wide")
# End of Dashboard setup

penguins = sns.load_dataset("penguins")

df = pd.read_csv('store.csv')

# Data preprocessing
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
# End of data preprocessing

with st.sidebar:
    st.title("Data Dashboard")
    st.markdown("Dashboard ini dibangun menggunakan library `streamlit` dengan perintah")
    st.code("import streamlit as st")
    with st.expander("Lebih detail untuk streamlit"):
        st.write(lorem.paragraph())
    freq = st.selectbox(
        "Pilih frekuensi",
        ('D','W','M','Q','Y')
        )
# End of sidebar

st.title("Penggunaan kolom")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", df['Sales'].sum())

with col2:
    st.metric("Total Quantity Shipped", df['Quantity'].sum())

with col3:
    st.metric("Number of Customers", df['Customer ID'].nunique())

col4, col5 = st.columns([1,3])
with col4:
    st.write(lorem.paragraph())
with col5:
    sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()
    st.line_chart(sales)

chrt1, chrt2 = st.columns([1,4])
with chrt1:
    fig1, ax1 = plt.subplots(figsize=(10,10))
    sns.scatterplot(
        data=df,
        x='Sales',
        y='Profit',
        ax = ax1
    )
    st.pyplot(fig1)

with chrt2:
    fig2, ax2 = plt.subplots(figsize=(16,3))
    sns.boxplot(
        data=df,
        x='Profit',
        y='Segment',
        ax = ax2
    )
    st.pyplot(fig2)

st.title('Menampilkan Teks')

st.write('Hello World!')

st.write(lorem.text())

st.markdown('# Ini heading 1')
st.markdown('## Ini heading 2')
st.markdown('`import streamlit as st`')

st.code('import pandas as pd')

st.latex('ax^2 + bx + c = 0')
st.markdown('---')

st.title("Dataframe dan metrics")
st.dataframe(df)
st.metric("# of Customers", df['Customer ID'].nunique(), "-10%")
st.metric("Total Sales", df['Sales'].sum(), "6%")
st.markdown('---')

st.title("Chart")
st.line_chart(sales)

st.markdown('---')

st.title('Input Methods')

st.write('Button')
click_me = st.button('Click me')
st.write(click_me)
# Challenge : Click me -> Click me again dst

st.write('Checkbox')
setuju = st.checkbox('Saya setuju')
if setuju:
    st.write('Terimakasih!')
else:
    st.write('Mohon centang kotak di atas')

st.write('Radio button')
jurusan = st.radio(
    'Mohon pilih jurusan kamu',
    ('Matematika', 'Fisika', 'Kimia', 'Biologi', 'Informatika')
)
st.write('Anda memilih jurusan ' + jurusan)

st.write('Select box')
buah = st.selectbox(
    'Mohon pilih buah buahan',
    ('Mangga', 'Jeruk', 'Apel')
)
st.write('Kamu memilih buah', buah)

st.markdown('---')

st.title("Multimedia")

image = Image.open('image.jpg')
st.image(image, caption='Ini gambar')

# Status
st.title("Status")

angka = st.number_input("Insert number", value=0, step=1)
if angka % 2 == 0:
    st.success("Genap")
else:
    st.error("Ganjil")