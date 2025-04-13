import streamlit as st
from transformers import pipeline
import fitz  # PyMuPDF for PDF
from newspaper import Article

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize text
def summarize_text(text):
    if len(text.strip()) == 0:
        return "⚠️ No text to summarize."
    return summarizer(text[:2000], max_length=100, min_length=30, do_sample=False)[0]['summary_text']

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Function to extract text from URL
def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return "❌ Failed to extract article. Please check the URL."

# Streamlit UI
st.title("📚 AI Text Summarizer")
st.write("Summarize text from input, PDFs, or web articles using a HuggingFace transformer model.")

# Choose input type
option = st.radio("Select Input Type:", ["Text", "PDF", "URL"])

input_text = ""

if option == "Text":
    input_text = st.text_area("Enter your text:", height=250)
    if st.button("Summarize Text"):
        st.markdown("### ✨ Summary:")
        st.write(summarize_text(input_text))

elif option == "PDF":
    uploaded_pdf = st.file_uploader("Upload a PDF file:", type=['pdf'])
    if uploaded_pdf is not None:
        pdf_text = extract_text_from_pdf(uploaded_pdf)
        if st.button("Summarize PDF"):
            st.markdown("### ✨ Summary:")
            st.write(summarize_text(pdf_text))

elif option == "URL":
    url = st.text_input("Enter a URL (e.g., news article):")
    if st.button("Summarize Article"):
        article_text = extract_text_from_url(url)
        if article_text.startswith("❌"):
            st.error(article_text)
        else:
            st.markdown("### ✨ Summary:")
            st.write(summarize_text(article_text))
