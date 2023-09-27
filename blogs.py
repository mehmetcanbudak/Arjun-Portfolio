import feedparser
import streamlit as st

@st.cache_data
def blogs():
    st.title("My Blogs 👾")
    rss_url = "https://medium.com/feed/@arjunprakash027"
    feed = feedparser.parse(rss_url)

    st.caption("Total Blogs: {}".format(len(feed.entries)))
    for item in feed.entries:
        title = item.title
        categories = [category.term for category in item.get('tags', [])]
        link = item.link
        published = item.published

        with st.expander(f"📖 {title}"):
            st.caption(published)
            st.link_button("Check blog here",link)
            st.write("Tags:",categories)