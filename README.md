# 📚 AI Text Summarizer

An AI-powered application that summarizes input text, PDFs, or news articles using state-of-the-art natural language processing. Built with **Streamlit** and powered by **Hugging Face Transformers**, this app simplifies long documents into concise summaries using **abstractive summarization**.

---

## 🚀 Features

- 📝 **Summarize Text**: Paste or type any block of text to get a short, meaningful summary.
- 📄 **Summarize PDFs**: Upload PDF documents and extract summaries automatically.
- 🌐 **Summarize URLs**: Extract and summarize articles from the web using `newspaper3k`.
- 🤖 **HuggingFace BART Model**: Uses `facebook/bart-large-cnn` for powerful abstractive summarization.

---

## 🧠 Model & Workflow

### 🔍 Model
- **Name**: `facebook/bart-large-cnn`
- **Type**: Abstractive summarization
- **Library**: HuggingFace Transformers

### 🔄 Workflow
1. User selects input type (Text, PDF, URL).
2. The app extracts text from the source.
3. The text is passed to the BART model for summarization.
4. The output summary is displayed in the app.

---

## 🛠 Installation

1. **Clone the repository**
  
   git clone https://github.com/your-username/ai-text-summarizer.git
   cd ai-text-summarizer

Install dependencies
pip install -r requirements.txt

Download required NLTK data
import nltk
nltk.download('punkt')

Run the Streamlit app
streamlit run summarizer.py
