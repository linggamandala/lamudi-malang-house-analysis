import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
from PIL import Image

st.set_page_config(layout='wide',
                   page_title='Analisis Penjualan Rumah di Kabupaten Malang (Lamudi Indonesia) Capstone Project',
                   page_icon=':house',
                   initial_sidebar_state='expanded')

# Header section
st.markdown("""
        <div style='text-align:center'>
                <h2>Analisis Penjualan Rumah di Kabupaten Malang (Lamudi Indonesia)</h2>
        </div>
        """, unsafe_allow_html=True)

header_image, header_write = st.columns(2)
with header_image:
        img=Image.open('images/sims_house.jpg')
        st.image(img)

with header_write:
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
                Dataset menggunakan hasil web scraping dan sudah dilakukan cleaning data. 
                \nUntuk mengaksesnya bisa klik link berikut 
                [lamudi_malang_dataset](https://github.com/linggamandala/lamudi-malang-house-analysis/blob/main/data/lamudi_malang_cleaned_data.csv)
                        """)
        st.sidebar.info("""
                        More info :
                        \n📧 [Email](linggarizkim@gmail.com)
                        \n🌐 [LinkedIn](https://www.linkedin.com/in/linggarizkim/)
                        \n🔗 [Github](https://github.com/linggamandala)
                        """)

# Load cleaned dataset
clean_df = pd.read_csv('data/lamudi_malang_cleaned_data.csv')

# Membagi tab dashboard
tab1, tab2, tab3, tab4 = st.tabs(['Harga rumah', 'Analisis', 'Kecamatan', 'Agen Lamudi'])

with tab1:
        # Visualisasi 1
        st.subheader('Harga penjualan rumah di Kabupaten Malang')

        # Mengetahui harga minimum, harga rerata, dan harga maksimum
        price_min, price_mean, price_max = st.columns(3)
        with price_min:
                harga_min = clean_df['price'].min() / 1_000_000
                st.metric('Harga minimum', value=f'IDR {harga_min:,.2f} juta')

        with price_mean:
                harga_mean = clean_df['price'].mean() / 1_000_000
                st.metric('Harga rerata', value=f'IDR {harga_mean:,.2f} juta')

        with price_max:
                harga_max = clean_df['price'].max() / 1_000_000_000
                st.metric('Harga maksimum', value=f'IDR {harga_max:,.2f} miliar')
                
        # Mencari LB minimum, LB rerata, dan LB maksimum
        luas_bangunan_min, luas_bangunan_mean, luas_bangunan_max = st.columns(3)
        with luas_bangunan_min:
                lb_min = clean_df['luas bangunan'].min()
                st.metric('Luas Bangunan minimum', value=f'{lb_min} m²')
                
        with luas_bangunan_mean:
                lb_mean = clean_df['luas bangunan'].mean()
                st.metric('Luas Bangunan rerata', value=f'{lb_mean:,.2f} m²')
                
        with luas_bangunan_max:
                lb_max = clean_df['luas bangunan'].max()
                st.metric('Luas Bangunan maksimum', value=f'{lb_max} m²')
                
        # Mencari LT minimum, LT rerata, dan LT maksimum
        luas_tanah_min, luas_tanah_mean, luas_tanah__max = st.columns(3)
        with luas_tanah_min:
                lt_min = clean_df['luas lahan'].min()
                st.metric('Luas Tanah minimum', value=f'{lt_min} m²')
                
        with luas_tanah_mean:
                lt_mean = clean_df['luas lahan'].mean()
                st.metric('Luas Tanah rerata', value=f'{lt_mean:,.2f} m²')
                
        with luas_tanah__max:
                lt_max = clean_df['luas lahan'].max()
                st.metric('Luas Tanah maksimum', value=f'{lt_max} m²')

        st.markdown('-------')

        st.subheader('Rumah Termurah')
        rumah_min, desc_rumah_min = st.columns(2)
        with rumah_min:       
                img_url = 'https://www.lamudi.co.id/dipasarkan-rumah-subsidi-murah-malang-169257392235.html'
                img=Image.open('images/rumah_malang_lamudi/rumah malang harga 100 juta.jpg')
                st.image(img)
                # st.subheader('[Harga rumah subsidi mulai IDR 100 juta](' + img_url + ')')
                st.markdown(f'<div style="text-align:center"><a href="{img_url}" target="_blank">Harga rumah subsidi mulai IDR 100 juta</a></div>', unsafe_allow_html=True)
                
        with desc_rumah_min:
                st.write("""
                        Dipasarkan Rumah Subsidi Murah Malang

                        Rumah Murah bersubsidi  Lokasi strategis mudah dijangkau DP bisa dicicil  Lokasi dekat kawasan Oma View Kota Malang (Jarak asli sesuai google maps) - 3 menit ke Oma View - 10 menit ke Gerbang Tol Kota Malang - 5 menit ke Indomart Kedungrejo - 5 menit ke SDN 1 Cemorokandang - 5 menit ke SMKN 9 Malang - 13 menit ke Kampus 2 Universitas Negeri Malang - 17 menit ke Rumah Sakit Puri Bunda - 22 menit ke Bandara Abdulrachman Saleh  Skema pembayaran : > DP bisa dicicil > KPR Subsidi Pemerintah Angsuran FLAT sampai LUNAS  Saat ini proses pembangunan 65 unit rumah  PROSES PENGEMBANGAN DI TAHAP 2 HINGGA 195 UNIT LAGI  Unit terbatas.   Buruan booking mumpung masih murah  Informasi Selanjutnya Hubungi marketing office kami dinomor tertera
                        """)

        st.markdown('-------')
        
        st.subheader('Rumah Termahal')
        rumah_max, desc_rumah_max = st.columns(2)        
        with rumah_max:
                img_url = 'https://www.lamudi.co.id/rumah-mewah-2-lantai-bonus-furnitur-kawasan-strate-16972585704.html'
                img=Image.open('images/rumah_malang_lamudi/rumah malang harga 4.08 miliar.jpg')
                st.image(img)
                # st.subheader('[Harga rumah mewah IDR 4.08 miliar](' + img_url + ')')
                st.markdown(f'<div style="text-align:center"><a href="{img_url}" target="_blank">Harga rumah mewah IDR 4.08 miliar</a></div>', unsafe_allow_html=True)
        
        with desc_rumah_max:
                st.write("""
                        Rumah Mewah 2 Lantai, Bonus Furnitur, kawasan strategis, Araya Malang

                        Rumah Mewah 2 Lantai di cluster paling bergengsi, furnitur lengkap, mudah perawatannya, berada di Lokasi strategis, terletak di antara 2 pintu Tol (Karanglo dan Pakis), dekat dengan Bandara Abd. Saleh, Persada Hospital serta Binus University, menggunakan One Gate Sistem, Jalan Cluster yang luas serta lingkungan yang asri HGB.  Lingkungan Hunian yang aman, nyaman terawat. Listrik 2200 W Air Sumur bor K. Tidur 3+ K. Mandi 4 Carport untuk 2 mobil Taman Rumah  Luas Tanah : 180 m2 Luas Bangunan :182 m2  Point of interest : 5 menit dari Bandara Abd Saleh 5 menit dari Gerbang Tol 3 Menit menuju ke Persada Hospital XXI Plaza Araya 2 Menit menuju ke 18 Holes Golf Course 1 Menit menuju Binus University 1 Menit dari Araya Arcade Garden 2 Menit dari Ombe Kofie 3 Menit dari Taman Indie Resto 3 Menit dari Sport Center Dekat dengan Tempat Ibadah  Lokasi : Cluster IXORA VALLEY, the Araya, Malang  Hubungi : Estate Property Titip Jual Beli Property
                        """)

with tab2:
        # Menghitung total rumah yang dijual terbanyak dari kecamatan
        st.subheader('List rumah yang dijual terbanyak di 10 Kecamatan Kab. Malang')
        bar1, bar2 = st.columns(2)
        with bar1:
                kecamatan = clean_df['kecamatan'].value_counts().head(10)
                top_10_kecamatan = clean_df[clean_df['kecamatan'].isin(kecamatan.index)]
                
                bar_chart = alt.Chart(top_10_kecamatan).mark_bar().encode(
                        x=alt.X('kecamatan:N', title='Kecamatan', sort='-y'),
                        y=alt.Y('count():Q', title='Jumlah Rumah (unit)'),
                        tooltip=[alt.Tooltip('kecamatan:N', title='Kecamatan'), alt.Tooltip('count():Q', title='Jumlah Rumah')]
                        ).properties(
                                width=500, height=500
                        ).interactive()
                st.altair_chart(bar_chart, use_container_width=True)

        with bar2:                
                st.write("""
                        Total rumah yang akan di jual di Kabupaten Malang sebanyak 1.763 unit. Adapun kec. Lowokwaru mendominasi penjualan rumah tertinggi dengan 381 unit. Disusul kec. Blimbing sebanyak 200 unit dan kec. Sukun sebanyak 173 unit. Setelah melakukan penelusuran, tiga kecamatan ini terletak di tengah Kota Malang. Dua kecamatan lainnya yaitu Kedungkandang dan Klojen menempati penjualan rumah masing-masing  sebanyak 108 dan 81 unit.""") 

                st.write("""
                        Total rumah yang akan dijual pada lima kecamatan yang terletak di tengah Kota Malang ini berjumlah 943 unit, atau sekitar 53.49% dari rumah yang akan dijual di Kabupaten Malang. Hal ini sangat menguntungkan calon pembeli yang akan tinggal di kawasan tengah Kota malang karena banyaknya penjualan rumah. """)

                st.write("""
                        Setelah ditelusuri lebih dalam, kec. Lowokwaru merupakan salah satu kecamatan yang mempunyai banyak perguruan tinggi. Tiga perguruan tinggi diantaranya adalah Universitas Brawijaya (UB), Universitas Negeri Malang (UM), dan Universitas Muhammadiyah Malang (UMM). Tentu hal ini sangat diuntungkan bagi calon properti untuk menyewakan atau mengontrak suatu rumah untuk hunian bagi mahasiswa baik yang berada disekitar kabupaten Malang maupun di luar untuk menuntut ilmu di kota pelajar ini.
                        """) 

        st.markdown('-------')

        #Menghitung banyaknya agen properti yang ada di Kab. Malang Lamudi ID
        st.subheader('Agen properti terbanyak di Kab. Malang')
        bar1, bar2 = st.columns(2)
        with bar1:
                agent = clean_df['agent_name'].value_counts().head(10)
                top_10_agent = clean_df[clean_df['agent_name'].isin(agent.index)]
                
                bar_chart = alt.Chart(top_10_agent).mark_bar().encode(
                        y=alt.X('agent_name:N', title='Nama Agen', sort='-x'),
                        x=alt.Y('count():Q', title='Jumlah Rumah (unit)'),
                        tooltip=[alt.Tooltip('agent_name:N', title='Nama Agen'), alt.Tooltip('count():Q', title='Jumlah Rumah')]
                        ).properties(
                                width=500, height=500
                        ).interactive()
                st.altair_chart(bar_chart, use_container_width=True)
        
        with bar2:
                st.write("""
                        10 Agen properti dengan penjualan rumah terbanyak di Kab. Malang. Dua diantaranya menempati penjualan rumah di atas 50 unit, yaitu Hwa Hwa merupakan agen Xavier Marks Premier Malang dan sastro merupakan agen Almahira Properti Malang. Adapun Asti Properti Malang merupakan agen Diamond Properti dan Iva Fiature merupakan agen Xavier Marks Premier Malang.""")

                st.write("""
                        Setelah melakukan penelusuran, Xavier Marks Premier Malang merupakan salah satu agen properti terbesar di Kab. Malang dan sudah berdiri sejak 2010. Sedangkan Almahira Properti Malang tidak ada info lebih lanjut, hanya mempunyai website saja. Hal yang sama juga tidak adanya informasi yang lebih lengkap pada agen Diamond Properti. """)
        

with tab3:
        # Menampilkan list data untuk pencarian rumah berdasarkan kecamatan
        st.subheader('List rumah yang akan dijual berdasarkan kecamatan di Kabupaten Malang')
        
        list_kecamatan = clean_df['kecamatan'].unique()
        selected_kecamatan = st.multiselect('Pilih Kecamatan:', list_kecamatan)
                
        if selected_kecamatan:
                filter_df = clean_df[clean_df['kecamatan'].isin(selected_kecamatan)]

                # Menampilkan slider untuk memfilter luas bangunan dan luas lahan
                # luas_bangunan_min, luas_bangunan_max = st.slider('Pilih Luas Bangunan (m²):', min_value=0, max_value=200, step=10, value=(0, 200))
                # luas_lahan_min, luas_lahan_max = st.slider('Pilih Luas Lahan (m²):', min_value=0, max_value=200, step=10, value=(0, 200))
                
                # Menampilkan input untuk memasukkan rentang harga
                cari_harga = st.number_input('Masukkan harga rumah yang ingin dicari:', min_value=100000000, step=10000000, max_value=4500000000)
                
                # Menampilkan input untuk memasukkan rentang luas bangunan
                cari_luas_bangunan = st.number_input('Masukkan luas bangunan (m²):', min_value=0, max_value=200)

                # # Menampilkan pilihan banyaknya kamar tidur
                # selected_kt = st.selectbox('Pilih banyaknya kamar tidur', options=[1,2,3,4,5,6,7], index=1)

                # Filter berdasarkan luas bangunan dan luas lahan
                # filter_df = filter_df[filter_df['kamar tidur'] == selected_kt]
                # filter_df = filter_df[(filter_df['luas bangunan'] >= luas_bangunan_min) & (filter_df['luas bangunan'] <= luas_bangunan_max)]
                # filter_df = filter_df[(filter_df['luas lahan'] >= luas_lahan_min) & (filter_df['luas lahan'] <= luas_lahan_max)]
                filter_df = filter_df[filter_df['price'] == cari_harga]
                filter_df = filter_df[filter_df['luas bangunan'] == cari_luas_bangunan]
                
                        
                if not filter_df.empty:
                        filter_df = filter_df.drop(['agent_status', 'description', 'kecamatan', 'kabupaten'], axis=1)
                        filter_df = filter_df.sort_values(by='price')
                        st.write('List rumah yang tersedia:', filter_df['title'].value_counts().sum(), 'unit')
                        st.write(filter_df.set_index(filter_df.columns[0]))
                else:
                        st.write('Tidak ada data.')
        else:
                pass
        
with tab4:
        # Menampilkan list data untuk pencarian rumah berdasarkan agen lamudi
        st.subheader('List rumah yang akan dijual berdasarkan agen Lamudi')
        list_agent = clean_df['agent_name'].unique()
        selected_agent = st.multiselect('Pilih nama agen:', list_agent)
        
        if selected_agent:
                agent_df = clean_df[clean_df['agent_name'].isin(selected_agent)]
                
                if not agent_df.empty:
                        agent_df = agent_df.drop(['agent_name', 'agent_status', 'description', 'kabupaten'], axis=1)
                        agent_df = agent_df.sort_values(by='price')
                        st.write('List rumah yang tersedia:', agent_df['title'].value_counts().sum(), 'unit')
                        st.write(agent_df.set_index(agent_df.columns[0]))
                else:
                        st.write('Tidak ada data untuk nama agen yang dipilih.')
        else:
                pass

st.markdown('-------')