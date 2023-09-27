import streamlit as st
import requests

@st.cache_data
def projects():
    st.title("My Projects 🤖")
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



@st.cache_data
def gists():
    language_containers = {}
    st.title("My Github Gists 📋")
    st.caption("Github gists are single file of code store in github")
    response = requests.get("https://api.github.com/users/arjunprakash027/gists")

    if response.status_code == 200:
        gists = response.json()
        # Print the names of all public repositories
        st.caption("Total Gists: {}".format(len(gists)))
        for gist in gists:
            for files in gist['files']:
                if gist['files'][files]['language'] not in language_containers.keys():
                    language_containers[gist['files'][files]['language']] = st.container()

        for name,container in language_containers.items():
            container.write(name)

        for gist in gists:
            for files in gist['files']:
                with language_containers[gist['files'][files]['language']]:
                    with st.expander(f"💥 {files}"):
                        st.link_button("Check code here",gist['html_url'])
                        st.write("language: {}".format(gist['files'][files]['language']))
                        st.write(gist["description"])

                        if gist['files'][files]['size'] < 9000:
                            code = requests.get(gist['files'][files]['raw_url'])
                            st.code(code.text)
                        else:
                            st.code("The size of the file is too large to display it!")

        
        
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")