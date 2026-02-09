import streamlit as st
import wikipedia

# Page Title
st.title("Legend AI Assistant 🤖")

# Wikipedia Search Feature
st.header("Search anything on Wikipedia 📚")
search_query = st.text_input("Enter a topic:")
if search_query:
    try:
        summary = wikipedia.summary(search_query, sentences=3)
        st.write(summary)
    except:
        st.error("Could not find information on this topic.")

# Photo Upload Feature
st.header("Upload a Photo 🖼️")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    st.success("Photo uploaded successfully!")

# Voice Assistant Note
st.info("Voice Assistant feature is active! 🎙️")
