import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from numerize import numerize

st.set_page_config(layout="wide")

st.write("Hello World!")
"potong bebek angsa. angsa dikuali. nona minta dangsa, dangsa empat kali. sorong ke kanan, sorong ke kiri. lalalala lalala lala. sorong ke kanan"
st.markdown("Nama saya **Ludy**")
st.markdown("---")

#ini judul dan subheader
st.title("Selamat datang Kaum ET")
st.subheader("Semoga Allah paring Aman Selamat Lancar Barokah")
#ini belajar masukin Code
st.code("import streamlit as st")

# Deklarasi dataset
df = pd.read_csv("store.csv")
st.dataframe(df)

# metrics
met1, met2, met3 = st.columns(3)
with met1:
    st.metric("Total Sales",
     "$ " + numerize.numerize(df['Sales'].sum()),
     "3.4%")
with met2:
    st.metric("Total Order", df['Order ID'].nunique())
with met3:
    st.metric("Number of Customer", df['Customer ID'].nunique())

# Sidebar
with st.sidebar:
    st.title("Dashboard Laporan Keuangan")
    freq = st.selectbox("Masukan Pilihan Warna Laporan", ('Merah', 'Kuning', 'Hijau', 'Biru', 'Ungu'))
    with st.expander("Ketahui lebih lanjut..."):
        st.write("Willington still in Progress. Keep Calm to success in your destination. See You with your choose...", freq)

# Data prep
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
# End of Data Prep
#Buat index dulu
freq = st.selectbox("Masukkan frekuensi", ('M', 'D', 'W', 'M', 'Q', 'Y'))
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()
#buat simple line charting
cap1, cht1 = st.columns([1,3])
with cap1:
    st.dataframe(sales)
with cht1:
    st.line_chart(sales)
## ini charting nonative
figi, ax1 = plt.subplots(figsize=(10,10))
sns.scatterplot(
    data = df,
    x='Sales',
    y='Profit',
    ax = ax1
)
st.pyplot(figi)
# Buat Button
st.title("Input")
tombol1= st.button("Tekan Tombol ini")
st.write(tombol1)

jurusan = st.selectbox(
    "Pilih Jurusan Kamu",
    ("Matematika", "Statistika", "Fisika", "Kimia")
)
st.write("Kamu memilih jurusan", jurusan)

setuju = st.checkbox("Centang Untuk Setuju")
if setuju:
    st.write("Anda sudah setuju")
else:
    st.write("Anda belum setuju")
nama = st.text_input("Masukkan inisial anda")
st.write("Halo sodara", nama)

#Image
image = Image.open("meme-python.png")
st.image(image, caption = "ini meme")

# buat charting se kolom 
st.title("Our Focus is in MSC and Data Science, Economics")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Mathematics** is the science and study of quality, structure, space, and change. Mathematicians seek out patterns, formulate new conjectures, and establish truth by rigorous deduction from appropriately chosen axioms and definitions.")
with col2:
    st.write("**Statistics** is the study and manipulation of data, including ways to gather, review, analyze, and draw conclusions from data. The two major areas of statistics are descriptive and inferential statistics.")
with col3:
    st.write("**Computational** is an adjective referring to a system of calculating or 'computing,' or, more commonly today, work involving computers. Tasks with a lot of computational steps are best performed on modern digital computers.")

col1, col2 = st.columns(2)
with col1:
    st.pyplot(figi)
with col2:
    st.line_chart(sales)
"Semua orang sangat bersemangat dan berlomba untuk kesuksesan mereka, baik di dunia maupun di akhirat"

angka = st.number_input("Masukkan angka", 0)
if angka %2==0:
    st.success("Angka Genap")
else:
    st.error("Angka ganjil")