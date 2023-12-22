import streamlit as st
import sys
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import pickle
import math

st.set_page_config(page_title="IPL PP PREDICTION", page_icon=":tada:")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



logo = Image.open("C:/Users/haris/Desktop/ML/Powerplay/logo.png")

with st.container():
    l,r=st.columns((1,3))
    with r:
        st.title("POWERPLAY PREDICTION")
    with l:
        st.image(logo)
st.write("---")

lottie_coding = load_lottieurl("https://lottie.host/50effd38-529f-42f2-bf92-0c97c01b485e/i3IYHKEI1d.json")
st_lottie(lottie_coding, height=300, key="coding")


st.subheader("Select the teams and venue to predict the Powerplay score")


def local_css(fn):
    with open(fn) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("C:/Users/haris/Desktop/ML/Powerplay/style.css")

# loading the saved model
loaded_model = pickle.load(open("C:/Users/haris/Desktop/ML/IPL powerplay Prediction/trained_model.sav", 'rb'))

team=["Chennai Super Kings","Delhi Capitals","Kolkata Knight Riders","Mumbai Indians","Punjab Kings","Rajasthan Royals","Royal Challengers Bangalore","Sunrisers Hyderabad"]
ground=['Kolkata', 'Mumbai', 'Pune', 'Delhi', 'Chennai', 'Hyderabad','Bangalore', 'Jaipur', 'Dharamsala']
team1=st.selectbox("Select Team1",options=team,placeholder="Team 1")
team2=st.selectbox("Select Team2",options=team,placeholder="Team 2")
g=st.selectbox("Select Ground",options=ground)



if team1==team2:
    st.warning("Select different teams")
    sys.exit()
    
    
t=[0]*8
t[team.index(team1)]=1
t1=[0]*8
t1[team.index(team2)]=1
t2=[0]*9
t2[ground.index(g)]=1
score=0
p=np.array(t+t1+t2).reshape(1,-1)
if st.button('PREDICT'):
    score=loaded_model.predict(p)
    st.subheader("The Average Powerplay Score of the Match is %d"%math.floor(score))
