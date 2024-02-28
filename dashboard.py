import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

st.set_page_config(layout='centered',
                   page_title='Analisis Penjualan Rumah di Kabupaten Malang (Lamudi Indonesia) Capstone Project',
                   page_icon=':house',
                   initial_sidebar_state='expanded')

# Header section
st.subheader("""
        Analisis Penjualan Rumah di Kabupaten Malang (Lamudi Indonesia)
        """)
img=Image.open('images/sims_house.jpg')
st.image(img, width=720)

st.write("""
        Properti merupakan salah satu aspek penting dalam kehidupan, khususnya bagi calon pasangan yang akan menikah ataupun pasangan yang sudah berkeluarga. Namun tidak sedikit yang paham tentang properti. Lamudi Indonesia sebagai salah satu platform properti yang sudah berdiri sejak Februari 2014 menghadirkan solusi untuk calon konsumen mencari hunian cocok maupun calon penjual yang akan menjual properti secara cepat dan tepat. 
        """)

st.write("""
        Untuk memahami penjualan properti pada Lamudi Indonesia, akan difokuskan pada penjualan rumah di Kabupaten Malang. Berikut di bawah ini akan dipaparkan hasil eksplorasi dan analisis.
        """)
st.markdown('-------')

# Side Section
with st.sidebar:
        st.header("""
                Analisis Penjualan Rumah di Kabupaten Malang (Lamudi Indonesia)
                """)
        st.write("""
                The Dashboard was created for DQLab TETRIS Batch 4 Capstone Project.
                """)
        st.write('Created by [Lingga Rizki Mandala](https://www.linkedin.com/in/linggarizkim/)')

# Load cleaned dataset
clean_df = pd.read_csv('data/lamudi_malang_cleaned_data.csv')

# Visualisasi 1
st.subheader('Penjualan rumah Lamudi Indonesia terbanyak di 10 kecamatan Kabupaten Malang')

kecamatan = clean_df['kecamatan'].value_counts().head(10)
top_10_kecamatan = clean_df[clean_df['kecamatan'].isin(kecamatan.index)]

plt.figure(figsize=(8, 8))
ax = sns.countplot(data=top_10_kecamatan, x='kecamatan', order=kecamatan.index)
ax.bar_label(ax.containers[0], fmt='%.0f', fontsize=10)
plt.xlabel('Kecamatan')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 1
st.write("""
        Kecamatan Lowokwaru mendominasi penjualan rumah di lamudi.co.id sebesar 459 unit. Kemudian disusul kecamatan Blimbing dengan jumlah 283 unit dan Kecamatan Sukun sebesar 198 unit. Adapun penjualan rumah di kecamatan Malang dan Kedungkandang masing-masing sebesar 139 dan 117 unit.
        """)
st.markdown('-------')

# Visualisasi 2
st.subheader('Harga penjualan rumah Lamudi Indonesia di Kabupaten Malang')

# Mengetahui harga minimum, harga rerata, dan harga maksimum
price_min, price_mean, price_max = st.columns(3)
with price_min:
        harga_min = clean_df['price'].min() / 1_000_000
        st.metric('Harga minimum', value=f'IDR {harga_min} juta')

with price_mean:
        harga_mean = clean_df['price'].mean() / 1_000_000_000
        st.metric('Harga rerata', value=f'IDR {harga_mean:,.2f} miliar')

with price_max:
        harga_max = clean_df['price'].max() / 1_000_000_000
        st.metric('Harga maksimum', value=f'IDR {harga_max:,.1f} miliar')
        
# Mencari LB minimum, LB rerata, dan LB maksimum
luas_bangunan_mean, luas_bangunan_max = st.columns(2)
# with luas_bangunan_min:
#         lb_min = clean_df['luas bangunan'].min()
#         st.metric('Luas Bangunan minimum', value=f'{lb_min} m²')
        
with luas_bangunan_mean:
        lb_mean = clean_df['luas bangunan'].mean()
        st.metric('Luas Bangunan rerata', value=f'{lb_mean:,.2f} m²')
        
with luas_bangunan_max:
        lb_max = clean_df['luas bangunan'].max()
        st.metric('Luas Bangunan maksimum', value=f'{lb_max} m²')
        
# Mencari LT minimum, LT rerata, dan LT maksimum
luas_tanah_mean, luas_tanah__max = st.columns(2)
# with luas_tanah_min:
#         lt_min = clean_df['luas lahan'].min()
#         st.metric('Luas Tanah minimum', value=f'{lt_min} m²')
        
with luas_tanah_mean:
        lt_mean = clean_df['luas lahan'].mean()
        st.metric('Luas Tanah rerata', value=f'{lt_mean:,.2f} m²')
        
with luas_tanah__max:
        lt_max = clean_df['luas lahan'].max()
        st.metric('Luas Tanah maksimum', value=f'{lt_max} m²')

# Analisis 2
st.write("""
        Harga penjualan rumah di Kabupaten Malang dibuka dengan harga IDR 100 juta dan maksimal di harga IDR 4.8 miliar. Luas tanah rata-rata sekitar 112 m² dengan luas bangunan 102 m². 
        """)

st.subheader('Harga rumah subsidi mulai IDR 100 juta')
img=Image.open('images/rumah_malang_lamudi/rumah malang harga 100 juta.jpg')
st.image(img, width=720)

st.subheader('Harga rumah mewah di kawasan Lowokwaru Malang IDR 4.8 miliar')
img=Image.open('images/rumah_malang_lamudi/rumah malang harga 4.8 miliar.jpg')
st.image(img, width=720)

st.markdown('-------')


# Visualisasi 3
st.subheader('Korelasi Harga Rumah terhadap Luas Bangunan')
plt.figure(figsize=(8,8))
sns.scatterplot(x='luas bangunan', y='price', data=clean_df)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 3
st.write("""
        Rumah dengan luas bangunan di bawah 150 m² dengan harga rentang hingga 2 miliar rupiah paling banyak. Dengan asumsi bahwa rumah yang untuk hunian luas bangunan rentang 25 m² hingga 150 m² merupakan mayoritas untuk diperjual belikan dan harga yang ditawarkan terjangkau untuk calon pembeli.
        """)
st.markdown('-------')

# Visualisasi 4
# st.subheader('Korelasi Harga Rumah terhadap Luas Tanah')
# # plt.figure(figsize=(10,8))
# sns.scatterplot(x='luas lahan', y='price', data=clean_df)
# st.set_option('deprecation.showPyplotGlobalUse', False)
# st.pyplot()

# # Analisis 4
# st.write("""
#         Sedangkan rumah dengan luas lahan yang lebih dari 50 m² hingga 150 m² mendominasi di harga rentang hingga 1.5 miliar.
#         """)
# st.markdown('-------')

# Visualisasi 5
st.subheader('Korelasi Banyaknya Kamar Tidur terhadap Luas Bangunan')
plt.figure(figsize=(6,6))
sns.scatterplot(x='kamar tidur', y='luas bangunan', data=clean_df)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 5
st.write("""
        Rumah dengan luas bangunan mulai dari 25 m² kebanyakan mempunyai 2 kamar tidur karena luasnya yang kecil. Sedangkan rumah dengan 3 kamar tidur bisa terlihat dengan luas bangunan mulai dari 50 m² ke atas.
        """)
st.markdown('-------')

# Visualisasi 6
st.subheader('Banyaknya agen properti Lamudi Indonesia di Kabupaten Malang')
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=top_10_kecamatan, x='kecamatan', hue='agent_status', order=kecamatan.index)
ax.bar_label(ax.containers[0], fmt='%.0f', fontsize=10)
ax.bar_label(ax.containers[1], fmt='%.0f', fontsize=10)
ax.bar_label(ax.containers[2], fmt='%.0f', fontsize=10)
plt.xlabel('Kecamatan')
plt.ylabel('Jumlah')
plt.xticks(rotation=30)
plt.legend(title='Status agen')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 6
st.write("""
        Terlihat bahwa status rekan lamudi pro dan rekan lamudi mendominasi agen penjualan rumah di website ini. Dengan fasilitas yang diberikan oleh lamudi dapat menguntungkan agen rekan lamudi, salah satunya adalah membantu agen penjualan rumah untuk mendapatkan calon pembeli yang berminat dan ingin mendapatkan rumah secara cepat.

        Bisa dilihat bahwa kecamatan Lowokwaru mendominasi banyaknya agen di lamudi.co.id. Antara rekan lamudi pro dengan rekan lamudi berbeda 2 orang saja. Selanjutnya pada kecamatan Blimbing selisih jauh antara rekan lamudi pro dan rekan lamudi dengan perbedaan 41 orang. Begitu juga dengan kecamatan lain yang mendominasi rekan lamudi pro dalam penjualan rumah di kabupaten Malang ini.
        """)
st.markdown('-------')

# Visualisasi 7
st.subheader('Top 10 agen properti Lamudi Indonesia terbanyak di Kabupaten Malang')
top_10_agent = clean_df['agent_name'].value_counts().head(10)
plt.figure(figsize=(12, 6))
ax = sns.barplot(x=top_10_agent.values, y=top_10_agent.index, orient='h')
ax.bar_label(ax.containers[0], fmt='%.0f', fontsize=10)
plt.xlabel('Jumlah Penjualan Rumah')
plt.ylabel('Nama Agen')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 7
st.write("""
        - Hwa Hwa merupakan agen Xavier Marks Premier Malang dan berstatus rekan lamudi sejak 2021.
        - Iva fiatur merupakan agen Xavier Marks Premier Malang dan berstatus rekan lamudi pro sejak 2021.
        - Sastro merupakan agen Almahira Properti Malang dan berstatus rekan lamudi pro sejak 2015.
        - Beni Sudiro merupakan agen Independent Agent dan berstatus rekan lamudi pro sejak 2017.
        - Asti Properti Malang merupakan agen Diamond Properti dan berstatus rekan lamudi sejak 2022.
        - Marketing Rumah & Konsultan KPR berstatus agen rekan lamudi pro.
        - Habibur Rohman merupakan agen Habibur Rohman Property dan berstatus rekan lamudi sejak 2021.
        - Myuu Naa merupakan agen rumah.malangbatu dan berstatus rekan lamudi sejak 2020.
        - Kiky Frediawan merupakan agen PROPERTi 81. Berstatus agent karena belum proses verifikasi di lamudi. Agen ini anggota sejak 2023.
        - Irma Naomi merupakan agen Xavier Marks Premiere Malang dan berstatus rekan lamudi sejak 2022.
        """)
st.markdown('-------')

# Visualisasi 8
st.subheader('Persentase agen properti Lamudi Indonesia di Kabupaten Malang')
agent_status_count = clean_df['agent_status'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(agent_status_count, labels=agent_status_count.index, autopct='%1.1f%%', startangle=90, colors=['orange', 'green', 'blue'])
plt.axis('equal')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Analisis 8
st.write("""
        Agen rekan lamudi pro menempati posisi pertama terbanyak dengan jumlah 50.5%, kemudian disusul rekan lamudi dengan jumlah 40.9%. Kedua status ini sudah terverifikasi oleh lamudi.co.id. Sedangkan Agent hanya status biasa dan belum terverifikasi di lamudi.co.id dengan jumlah 8.7%.
        """)
st.markdown('-------')

# Kesimpulan
st.subheader("""
            Conclusion
            """)

st.write("""
        Berdasarkan hasil visualisasi di atas, dapat disimpulkan sebagai berikut:
        1. harga penjualan rumah di Kabupaten Malang (lamudi.co.id) mulai dari Rp. 100 juta hingga Rp 4.8 miliar.
        2. Banyaknya rumah dengan luas bangunan 25 m² hingga 150 m² dengan rentang harga Rp. 100 juta hingga Rp. 2 miliar.
        3. Adapun rumah dengan luas bangunan di atas memiliki banyaknya kamar tidur dari 2 - 4 kamar.
        4. Mayoritas penjualan rumah yang paling banyak terdapat pada kecamatan Lowokwaru kabupaten Malang dengan jumlah 459 unit. Sedangkan kecamatan Blimbing dan kecamatan Sukun masing-masing dengan jumlah 283 dan 198 unit.
        5. Banyaknya agen rekan lamudi karena sudah terverifikasi lamudi.co.id. Dengan persentase rekan lamudi sebanyak 40.9% dan rekan lamudi pro sebanyak 50.5%.
        6. Dari banyaknya agen lamudi.co.id yang menjual properti rumah, ternyata banyak agen-agen properti di luar lamudi.co.id dimana salah satunya adalah Xavier Marks Premier Malang yang merupakan agen properti terbesar di Malang dan mempunyai perkantoran.
        """)

st.markdown('-------')