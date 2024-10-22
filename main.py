import streamlit as st
import asyncio
from scrape import (scrape_website, extract_content, split_dom)
from llmin import parse_with_llm

async def main():
    st.title("Webalyze")
    url = st.text_input("Enter a website URL: ")

    if st.button("Scrape Website"):
        st.write("Scraping the website")
        content = await scrape_website(url)
        clean_content = extract_content(content)

        st.session_state.dom_content = clean_content
        print(clean_content)

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", clean_content, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("What do you wanna parse bro?")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content")
                dom_chunks = split_dom(st.session_state.dom_content)
                res = parse_with_llm(dom_chunks, parse_description)
                st.write(res)


if __name__ == "__main__":
    asyncio.run(main())
