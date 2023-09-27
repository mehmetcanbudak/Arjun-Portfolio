import streamlit as st
import pandas as pd

def graph_of_what_i_know():
    st.graphviz_chart(
        '''
        digraph {
        me -> Backend
        me -> Frontend
        me -> Data_science
        me -> DevOps
        me -> Experimenting
        Frontend -> React
        Backend -> Monolith,Microservices,Databases
        Databases -> MySql,Postgresql,MongoDB 
        Monolith -> Django
        Microservices -> FastApi,Flask,Redis
        Data_science -> Machine_Learning,Data_Analytics
        Machine_Learning -> Algorithms,MLOps
        MLOps -> Backend
        Data_Analytics -> SQL,EDA_in_Python
        DevOps -> Git,Docker
        Experimenting -> Fine_Tuning,Vector_DB,GO,Rust
        Fine_Tuning -> BERT,CLIP,Falcon7b
        }
        '''
    )

def education():
    df = pd.DataFrame(
        {
            "Study" : ["BTech","12th Grade"]
        }
    )


def stuff_i_know():
    st.title("MY STACK 💻")
    graph_of_what_i_know()