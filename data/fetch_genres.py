# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:46:19 2020

@author: Daniel Brunnsåker
"""
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

def fetch_htmldata(url):

    try:
        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, "html.parser")
        return soup
    except:
        print("An error occured while parsing soup")
    
    

def fetch_genres(soup):
    
    try:
        mydivs = soup.findAll("div", {"class": "meta-value"})
        rating = mydivs[0].text
        txt = mydivs[1].text
        genres = re.findall(r'(?<!^)(?<!\. )[A-Z][a-z]+',txt)
        
        return genres, rating
    
    except:
        print("An error occured when collecting genres")

def replace_symbols(df):
    df = df.replace('[^\w ]', '', regex=True)
    df = df.replace(' ', '_', regex=True)
    return df
    

titles = pd.read_csv('movie_titles.txt')
titles = replace_symbols(titles)
data = pd.DataFrame()


for idx,name in titles.iterrows():
    print(name[0])
    url = str('https://www.rottentomatoes.com/m/'+name[0])
    soup = fetch_htmldata(url)
    genres, rating = fetch_genres(soup)
    
    collection = [name[0],genres,rating]
    pd.concat([data,collection])


