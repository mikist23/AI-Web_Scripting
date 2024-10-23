import streamlit as st
from srape import scrape_website

st.title("AI Web 🦜🛠️ Scraper")

url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping he website")
    result = scrape_website(url)
    print(result)