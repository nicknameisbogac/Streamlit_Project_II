# imports
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#CSV_FILE="D:\\_Kunta_Kinte\\Streamlit\\Streamlit_Trainings\\Serce_Egitim_Data.csv"
#JPG_FILE="D:\\_Kunta_Kinte\\Streamlit\\Streamlit_Trainings\\serce.jpg"
#CSV_FILE=r"F:\\_Kunta_Kinte\\Streamlit\\Streamlit_Trainings\\Serce_Egitim_Data.csv"
#JPG_FILE=r"F:\\_Kunta_Kinte\\Streamlit\\Streamlit_Trainings\\serce.jpg"

# functions
#@st.cache()
def Veri_Yukle():
    """
    df = pd.read_csv(
        #'https://github.com/nicknameisbogac/Streamlit_Project_II/blob/master/Serce_Egitim_Data.csv?raw=True', \
        CSV_FILE, \
        sep=';')
    """
    
    """
    df = pd.read_csv( \
        'https://github.com/nicknameisbogac/Streamlit_Project_II/blob/master/Serce_Egitim_Data.csv', \
        sep=';')
    """
    
    df = pd.read_csv( \
         'https://raw.githubusercontent.com/nicknameisbogac/Streamlit_Project_II/main/Serce_Egitim_Data.csv', \
        sep=';')
    return df
                     
def Menu_Sakla():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} # Hide Hamburger Menu
    #if you change "Made With Streamlit"
    #footer {
    #visibility: hidden;
    #}
    #footer:after {
    #content:'goodbye'; 
    #visibility: visible;
    #display: block;
    #position: relative;
    #background-color: red;
    #padding: 5px;
    #top: 2px;
    #}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    return 0

def Menu_Olustur():
    Options_Tuple = ("Yayılım Grafikleri", "Bar Grafikleri")
    
    """
    #with Image.open(JPG_FILE) as Img:
    with Image.open(JPG_FILE) as Img:
        width, height = Img.size # get the image size...
        # Provide the target width and height of the image
        if ((width > 200) or (height > 200)):
            width, height = 200, 200 # (im.width // 2, im.height // 2)
            Img_Resized = Img.resize((width, height))
    
    
    st.sidebar.image(Img, use_column_width = True)
    """
    
    
    st.sidebar.markdown("<h1 style='text-align: center; color: red;'>Serçe Eğitim Kurumu</h1>", unsafe_allow_html=True)    
    st.sidebar.markdown("<h1 style='text-align: center; color: red;'>Grafik Raporlama</h1>", unsafe_allow_html=True)    
    
    Option = st.sidebar.selectbox(label="Seçiminiz...", options = Options_Tuple, index = 0)
    
    with st.sidebar.expander('Hakkında', expanded = False):
        st.info("2021 yılında geliştirildi.")
        
    return Option, Options_Tuple

def main():
    Menu_Sakla()
    df = Veri_Yukle()
    Option, Options_Tuple = Menu_Olustur()

    if Option == Options_Tuple[0]: #"Yayılım Grafikleri"
        st.markdown("<h1 style='text-align: center; color: blue;'>5. Sınıflar Değerlendirme Sınavı Sonuçları</h1>", unsafe_allow_html=True)    

        x_ekseni_sec = ['Mat_P', 'Fen_P', 'Ing_P', 'Tur_P', 'Sos_P']
        x_eksen_sidebar = st.selectbox('Hangi Ders Değerlendirmesi ?', x_ekseni_sec)
        fig = px.scatter(df,
                         x=x_eksen_sidebar,
                         y="Basari_Notu",
                         hover_name="Kampus",
                         title=f"Başarı Notu ile {x_eksen_sidebar} Karşılaştırması")
        st.plotly_chart(fig)
    elif Option == Options_Tuple[1]: #"Bar Grafikleri"
        st.markdown("<h1 style='text-align: center; color: blue;'>5. Sınıflar Değerlendirme Sınavı Sonuçları</h1>", unsafe_allow_html=True)    

        Ders_Puan=["Kampus", "Mat_P","Fen_P","Ing_P","Tur_P","Sos_P","Basari_Notu"]
        df_Indirgenmis=df.groupby("Kampus")[Ders_Puan].mean().reset_index()
        with st.expander("Kampüs Bazında"):
            fig = px.bar(df_Indirgenmis,
                             x='Kampus',
                             y="Basari_Notu",
                             color='Kampus',
                             orientation = 'v',
                             title=f"Başarı Notuna Göre Kampüsler")
            st.plotly_chart(fig)
        with st.expander("Kampüs\Sınıf Bazında"):
            Kampus_Tuple=tuple(df["Kampus"].unique())
            Kampus_Sec=st.selectbox("Kampüs Seçiniz...", Kampus_Tuple)
            Kriter = df["Kampus"] == Kampus_Sec
            df_Indirgenmis=df.loc[Kriter]
            df_Kampus_Sinif=df_Indirgenmis.groupby("Sinif")["Basari_Notu"].mean().reset_index().round(1)
            fig = px.bar(df_Kampus_Sinif,
                             x='Sinif',
                             y="Basari_Notu",
                             color='Sinif',
                             orientation = 'v',
                             title=f"{Kampus_Sec} Kampüsü 5. Sınıfların Ortalama Başarı Notu")
            st.plotly_chart(fig)

    elif Option == Options_Tuple[2]: # 
        pass
        """
        st.text("Bugün : " + Tarih_Saat()[0])
        Islenen_Dosya = file_uploaders()
        if Islenen_Dosya is not None:
            st.write(Islenen_Dosya)
        """

if __name__ == '__main__':
    main() 
