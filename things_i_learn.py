import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json

#loading the secret for my notion page
@st.cache_data
def learnings():
    st.title("Resources Database")
    st.write("I document all the resources that i learn from in an notion database. \n Here are those straight from my notion database.")

    load_dotenv()
    secret = os.getenv("SECRET")

    headers = {
        'Authorization':f"Bearer {secret}",
        'Content-Type':'application/json',
        'Notion-Version':'2022-06-28'}

    headers_get = {
        'Authorization': f'Bearer {secret}',
        'Notion-Version': '2021-08-16'
    }

    search_params = {"filter": {"value": "page", "property": "object"}}
    search_response = requests.post(
        f'https://api.notion.com/v1/search', 
        json=search_params, headers=headers)

    for pages in search_response.json()['results']:
        # print(len(search_response.json()['results']))
        page_id = pages['id']
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        response = requests.get(url,headers=headers_get)
        try:
            with st.expander(f"🦄 {pages['properties']['Name']['title'][0]['plain_text']}"):
                for study_detail in response.json()['results']:
                    try:
                        st.link_button(study_detail['paragraph']['text'][0]['plain_text'],study_detail['paragraph']['text'][0]['href'])
                    except:
                        pass
        except:
            pass




