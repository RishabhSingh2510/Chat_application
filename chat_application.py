import streamlit as st
import os
import random
import glob 
from datetime import datetime as dt
import json
from urllib import parse, request
import urllib.request as url
import bs4

greetintent = ['hi','hello','hey','hello there','hi there']   #you can add more terms that you want youe application to understand
dateintent = ['date','tell me date','please tell me date']
timeintent = ['time','tell me time','please tell me time']
musicintent = ['music','play music','please play music']
giphyintent = ['giphy','get giphy']
shoppingintent = ['shop','buy','order']

st.set_page_config(
    page_title='chat app',            #title of tab
    layout = 'wide'
)

st.title("steamlit chat application....") #heading
st.write("try saying hi or play music or tell me date") #as a paragraph

form = st.form("chat_form") #making form
msg = form.text_input("enter your message...") #taking input
btn = form.form_submit_button("send message") #sumbit button

if btn:
    msg = msg.lower()
    if msg in greetintent:
        st.write("Hello")
    elif msg == 'ram ram':
        st.write("JAI SHREE RAM...")
    elif msg in shoppingintent:
        product = form.text_input("enter electronic product: ")
        product = product.replace(" ","+").lower()
        for k in range(1,6):
            path = f"https://www.flipkart.com/search?q={product}&page={k}"   #you can change the path to the site from where you want your data.
            st.write(url.urlopen(path))
            response = url.urlopen(path) #making html request
            page = bs4.BeautifulSoup(response,"lxml") 
            titlelist = page.find_all("div",{'class':'_4rR01T'})
            pricelist = page.find_all("div",{'class':'_30jeq3 _1_WHN1'})
            for i in range(len(titlelist)):
                st.write(titlelist[i].text)
                st.write(pricelist[i].text)
                st.write("*"*30)
    elif msg in giphyintent:
        a = form.text_input('enter the subject of the Giphy: ').strip()
        n = form.text_input("how many: ")
        url = "http://api.giphy.com/v1/gifs/search"

        params = parse.urlencode({
        "q": a,
        "api_key": "9rwNV6zq4kdE8ir1Q2AAQSV0AfG3d8wx",   #you can get your api_key from https://developers.giphy.com
        "limit": n
        })

        with request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())

        gif_images = data['data']
        for i in range(len(gif_images)):
            path = gif_images[i]['images']['original']['url']
            request.urlretrieve(path,f'img_{i}.gif')
            st.write(f'downloaded {i+1} images')
    elif msg in dateintent:
        date = dt.now().date()
        st.write("date is",date.strftime("%d %B %Y, %A")) #B Y A
    elif msg in timeintent:
        time = dt.now().time()
        st.write("time is:",time.strftime("%H:%M:%S, %p"))
    elif msg in musicintent:
        path = r"C:\\Users\\ASUS\\Desktop\\tt\\1st" #giving path of music folder where you have mp3 music file
        os.chdir(path) #changing directory
        songs = glob.glob("*.mp3") #listing all mp3 songs, you can chage the format or add other formats to the list also.
        # st.write(songs)
        play = random.choice(songs) #selecting random fromm song list
        os.startfile(play) # starting any file
    elif msg == 'bye':
        st.write("Bye ...")

    else:
        st.write('i dont understand')  #the statement which will be displayed if unrecognizable input is given
