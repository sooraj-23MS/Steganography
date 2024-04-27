import streamlit as st
from PIL import Image
from audmain import AudioSteg
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="MiniProject",layout="wide")
with st.sidebar:
    selected=option_menu(
        menu_title="Types :",
        options=["Image","Audio"],
        default_index=0,
    )
if selected == "Image":
 from imgmain import ImageSteg

 
 st.title(" Image Steganography ")
 stat = st.radio("FUNCTIONS :", ('ENCode', 'DECode'))
 if (stat == 'ENCode'):
          st.header("Encoding Part :")
          ima = st.text_input("Image Path >>",'')
          msg = st.text_area("Enter Message >> ", "")
          sckey = st.text_input("Enter Key >>")
          path1 = st.selectbox("Target Path >>",["Folder 1","Folder 2"])
          if st.button("ENCode"):
           img = ImageSteg()
           img.encrypt_text_in_image(ima,msg,path1+"/")
           st.success("Encoded Successfully")
           col1, col2 = st.columns(2)
           col1.header("selected Image :")
           original = Image.open(ima)
           col1.image(original, use_column_width=True)


 if (stat == 'DECode'):
    st.header("Decoding Part :")
    imp= st.text_input("Image Path >> ",'')
    exkey = st.text_input("Enter Key >>")
    loc = st.selectbox("Target Path >>",["Folder 1","Folder 2"])
    if st.button("DECode"):
     img = ImageSteg()
     res = img.decrypt_text_in_image(loc+"/"+imp)
     st.success(res)


if selected == "Audio":
   def encode_message(aud):
    # Encode
    st.header("Encoding Part :")
    msg = st.text_area("Write a message: ")
    audio = st.text_input("Name the audio wave file: ")
    newfile = st.text_input("Enter the new filename: ")
    key = st.text_input("Enter the stego key: ")
    if st.button("Encode"):
        if msg and audio and newfile and key:
         aud.encod( audio, msg, key, newfile)
         isExist = os.path.exists(audio + '.wav')
         if isExist is False:
          st.toast("file not found")
          
         else:
            st.success("Message encoded ")
        else:
         st.toast("Please fill in all the fields.")

   def decode_message(aud):
    # Decode
    st.header("Decoding Part :")
    filename = st.text_input("Name the audio wave file (only if is in the same folder): ")
    reference_key = st.text_input("Enter the stego key: ")
    if st.button("Decode"):
        if filename and  reference_key:
         dmsg = aud.decod(filename, reference_key)
         isExist = os.path.exists(filename + '.wav')
         if isExist is False:
             st.toast("file not found")
         else: 
           st.success(dmsg)
        else:
         st.toast("Please fill in all the fields.")

   def main():

    
    #st.markdown('<style>' + open('custom.css').read() + '</style>', unsafe_allow_html=True)
    st.title(" Audio Steganography ")
    aud = AudioSteg()
    stat = st.radio("FUNCTIONS  :", ('Encode', 'Decode'))

    if(stat == 'Encode' ):
        encode_message(aud)
    if (stat == 'Decode'):
        decode_message(aud)



   if __name__ == "__main__":
    main()
    