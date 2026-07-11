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
    p="You are an Art Analyst and Art Critic. Only answer questions related to art. If the user asks anything outside this topic, politely respond that you can only assist with art-related questions."
    final_prompt = f"You are an AI Art Critic and Art Analyst. Answer only art-related questions. If a question is unrelated to art, politely say that you can only help with art analysis and criticism. Respond in {b} language."
    res=model.generate_content([prompt,img,final_prompt])
    st.write(res.text)
    c=gTTS(res.text)
    c.save("output.mp3")
    st.audio("output.mp3")
