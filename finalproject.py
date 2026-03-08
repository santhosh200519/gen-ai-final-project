import streamlit as st
from PIL import Image
import google.generativeai as genai
from gtts import gTTS
genai.configure(api_key="AIzaSyBsbLlJPDmUPBchoVBm7INPwdGrKUUNMPc")
model=genai.GenerativeModel('gemini-2.5-flash')
st.title("🎨AI Art Critic")
st.header("art")
lang={"English":"en","Tamil":"ta","Hindi":"hi"}
b = st.selectbox("Select Language",lang.keys())
d=lang[b]
i=st.file_uploader("Upload here",('jpg','png','jpeg'))
prompt=st.text_input("Ask here: ")
if st.button('submit') and prompt:
    img=Image.open(i)
    p='you are act as a art analyst and art critic, if user is ask other than told out of that topic'
    final_prompt = f"You are an AI art critic and art analyst.Answer ONLY about the art.Respond in {b} language."
    res=model.generate_content([prompt,img,final_prompt])
    st.write(res.text)
    c=gTTS(res.text)
    c.save("output.mp3")
    st.audio("output.mp3")