import streamlit as st
from crawl4ai import WebCrawler
import base64
import time

def download_markdown(content, filename="extracted_content.md"):

    b64 = base64.b64encode(content.encode()).decode()

    href = f'<a href="data:file/markdown;base64,{b64}" download="{filename}">📥 Download Markdown File</a>'
    return href

def add_custom_css():
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 8px 16px;
        font-size: 16px;
    }
    .stTextInput>div>input {
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #ccc;
    }
    .download-link a {
        font-size: 18px;
        color: #007BFF;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    add_custom_css()  

    st.title("🔎 Crawl4AI Web Scraper")
    

    
    url = st.text_input("🌐 Enter the URL you want to scrape:", "")


    if st.button("Run Crawl"):
        if url:
            with st.spinner("🕵️‍♂️ Crawling the web page..."):
            
                crawler = WebCrawler()
                crawler.warmup()
                
        
                time.sleep(2)  


                result = crawler.run(url=url)
                st.success("✅ Crawl completed successfully!")
                st.subheader("📝 Extracted Content")
                st.markdown(result.markdown)
                st.markdown(
                    f'<div class="download-link">{download_markdown(result.markdown)}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.warning("⚠️ Please enter a valid URL.")

if __name__ == "__main__":
    main()
