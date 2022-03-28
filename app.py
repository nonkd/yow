# import module
import streamlit as st
 
# Title
st.title("Manfaat Biji-Bijian Buah")

# Header
st.header("Yuk cari tau manfaat biji-bijian buah!")
 


#from PIL import Image
#img1 = Image.open("Almond (61).jpg")
#img2 = Image.open("Amla (61).jpg")
#img3 = Image.open("Apple (61).jpg")
#img4 = Image.open("Avocado (61).jpg")
#img5 = Image.open("Betel_Nut (63).jpg")
#img6 = Image.open("Black_Plum (61).jpg")


domain = st.selectbox("Biji buah yang kamu cari: ",
					['','Almond', 'Amla', 'Apple', 'Avocado','Betel Nut','Black Plum'])

if (domain == ''):
	st.write("")
elif(domain == 'Almond'):
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img1, width=200)
	st.write("Manfaat biji Almond adalah menurunkan resiko pernyakit kanker, mengelola kadar kolesterol darah, menstabilkan tekanan darah, mencegah penyakit jantung, mengendalikan kadar gula darah, menurunkan berat badan.")
elif (domain == 'Amla'):
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img2, width=200)
	st.write("Manfaat biji Amla adalah menyehatkan kulit, meningkatkan kekebalan tubuh, mengontrol kadar gula darah, melindungi sel-sel otak, menurunkan beart badan.")
elif (domain == 'Apple'):
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img3, width=200)
	st.write("Manfaat biji Apple adalah membantu membunuh sel kanker di dalam tubuh.")
elif (domain == 'Avocado'):
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img4, width=200)
	st.write("Manfaat biji Avocado adalah kaya antioksidan, sumber potasium yang baik, mencegah kanker, menyembuhkan gangguan pencernaan, menghambat infeksi jamur.")
elif (domain == 'Betel Nut'):
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img5, width=200)
	st.write("Manfaat biji Betel Nut adalah menjaga kesehatan dan kebersihan mulut, menjaga kesehatan dan kebersihan mulut dan melancarkan pencernaan.")
else:
	#st.write("Ini adalah gambar dari biji buah yang kamu cari")
	#st.image(img6, width=200)
	st.write("Manfaat biji Black Plum adalah meningkatkan sistem imun, menjaga kesehatan jantung, mencegah penyakit kanker, menjaga kesehatan mata dan melancarkan pencernaan.")

domain1 = st.multiselect("Pilih biji-bijian yang pernah kamu manfaatkan: ", 
	['Almond', 'Amla', 'Apple', 'Avocado','Betel Nut','Black Plum'])

if domain1:
	st.text(st.write("Kamu sudah memanfaatkan sebanyak", len(domain1), 'biji buah-buahan'))

lain = st.text_area("Tuliskan manfaat buah yang lain", " ")
if(st.button('Submit')):
	result = lain.title()
	st.success(result)

if(st.button("Pesan untukmu")):
	st.text("Terimakasih, tetap semangat ya!!! :))")
