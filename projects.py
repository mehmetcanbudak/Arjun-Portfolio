import streamlit as st
import requests

@st.cache_data
def projects():
    st.title("My Projects 🤖")
    st.balloons()
    ignore_list = ['arjunprakash027','collections','Django_application']
    response = requests.get("https://api.github.com/users/arjunprakash027/repos")

    if response.status_code == 200:
        repos = response.json()
        print(len(repos))
        # Print the names of all public repositories
        st.caption("Total Projects: {}".format(len(repos)))
        for repo in repos:
            if repo['name'] not in ignore_list:
                topic_string = ""
                with st.expander(f"🔥 {repo['name']}"):
                    st.link_button("Check code here",repo['html_url'])
                    st.write(repo["description"])
                    for topic in repo['topics']:
                        topic_string += f"#{topic}  "
                    st.info(topic_string)
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")