import streamlit as st
import nltk
import spacy
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import time



st.set_page_config(
    page_title="Smart NLP Dashboard",
    page_icon="🤖",
    layout="wide"
)



st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1,h2,h3,h4,h5 {
    color: white;
}

textarea {
    font-size: 18px !important;
}

.block {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #333;
}

</style>
""", unsafe_allow_html=True)



nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')



nlp = spacy.load("en_core_web_sm")



st.sidebar.title("📌 About Project")

st.sidebar.info("""
This is an AI-powered NLP Dashboard developed using:

✅ Python  
✅ Streamlit  
✅ NLTK  
✅ spaCy  
✅ TextBlob  
✅ Matplotlib  

The system performs:

• Tokenization  
• Stopword Removal  
• Sentiment Analysis  
• Named Entity Recognition  
• Word Frequency Analysis  
• Text Summarization  
• Word Cloud Visualization
""")



st.markdown("""
<h1 style='text-align:center; color:#4CAF50;'>
🤖 Smart NLP Text Analyzer Dashboard
</h1>

<h4 style='text-align:center;'>
Natural Language Processing using Artificial Intelligence
</h4>

<hr>
""", unsafe_allow_html=True)



st.markdown("## 🚀 NLP Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("✅ Tokenization")
    st.success("✅ Stopword Removal")
    st.success("✅ Sentiment Analysis")

with c2:
    st.success("✅ Named Entity Recognition")
    st.success("✅ Word Frequency Analysis")

with c3:
    st.success("✅ Text Summarization")
    st.success("✅ Word Cloud Visualization")

st.markdown("---")



text = st.text_area(
    "✍️ Enter your text here",
    height=220
)



if st.button("🚀 Analyze Text"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")

    else:

        with st.spinner("Analyzing text using NLP..."):
            time.sleep(1)

    

        tokens = word_tokenize(text)

      

        stop_words = set(stopwords.words('english'))

        filtered_words = [
            word for word in tokens
            if word.lower() not in stop_words and word.isalpha()
        ]

    

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

     

        doc = nlp(text)

        entities = []

        for ent in doc.ents:
            entities.append({
                "Entity": ent.text,
                "Label": ent.label_
            })

  

        word_freq = Counter(filtered_words)

        top_words = word_freq.most_common(10)



        sentences = text.split(".")

        if len(sentences) >= 2:
            summary = sentences[0] + "." + sentences[1]
        else:
            summary = text


        st.markdown("## 📊 Dashboard Metrics")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Total Tokens", len(tokens))
        m2.metric("Filtered Words", len(filtered_words))
        m3.metric("Named Entities", len(entities))
        m4.metric("Unique Words", len(set(filtered_words)))

        st.markdown("---")

        st.markdown("## 📝 Tokenization")

        st.info(
            "Tokenization splits text into individual words or tokens."
        )

        st.write(tokens)

        st.markdown("---")



        st.markdown("## 🚫 Stopword Removal")

        st.info(
            "Stopwords like 'is', 'the', 'and' are removed."
        )

        st.write(filtered_words)

        st.markdown("---")

  

        st.markdown("## 😊 Sentiment Analysis")

        st.info(
            "Sentiment analysis identifies emotional tone."
        )

        if sentiment > 0:

            st.success("Positive Sentiment 😀")

        elif sentiment < 0:

            st.error("Negative Sentiment 😔")

        else:

            st.warning("Neutral Sentiment 😐")

        st.write("### Sentiment Score")
        st.write(sentiment)

        st.markdown("---")

    

        st.markdown("## 🏷️ Named Entity Recognition")

        st.info(
            "NER detects names, locations, organizations, dates etc."
        )

        if len(entities) > 0:

            entity_df = pd.DataFrame(entities)

            st.dataframe(entity_df)

        else:

            st.warning("No entities found.")

        st.markdown("---")


        st.markdown("## 📄 Text Summarization")

        st.info(
            "Summarization extracts important information."
        )

        st.success(summary)

        st.markdown("---")

        st.markdown("## 📊 Word Frequency Analysis")

        st.info(
            "Shows most repeated words in the text."
        )

        freq_df = pd.DataFrame(
            top_words,
            columns=["Word", "Frequency"]
        )

        st.table(freq_df)

 

        st.markdown("### 📈 Frequency Chart")

        words = [word[0] for word in top_words]
        counts = [word[1] for word in top_words]

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(words, counts)

        ax.set_xlabel("Words")
        ax.set_ylabel("Frequency")
        ax.set_title("Top Frequent Words")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        st.markdown("---")


        st.markdown("## ☁️ Word Cloud Visualization")

        st.info(
            "Word cloud visually represents important words."
        )

        wordcloud = WordCloud(
            width=1200,
            height=500,
            background_color='white',
            colormap='viridis'
        ).generate(text)

        fig2, ax2 = plt.subplots(figsize=(14, 7))

        ax2.imshow(wordcloud)

        ax2.axis("off")

        st.pyplot(fig2)



st.markdown("---")

st.markdown("""
<center>
Developed using Python, Streamlit, NLTK, spaCy, TextBlob and Matplotlib
</center>
""", unsafe_allow_html=True)