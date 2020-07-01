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
    except:
        print("An error occured.")
    
    soup = BeautifulSoup(data, "html.parser")
    return soup

def fetch_genres(soup):
    
    mydivs = soup.findAll("div", {"class": "meta-value"})

    txt = mydivs[1].text
    genres = re.findall(r'(?<!^)(?<!\. )[A-Z][a-z]+',txt)
        
    return genres

def replace_symbols(df):
    df = df.replace('[^\w ]', '', regex=True)
    df = df.replace(' ', '_', regex=True)
    return df
    

titles = pd.read_csv('movie_titles.txt')
titles = replace_symbols(titles)

movies_url = 'https://www.rottentomatoes.com/m/you_should_have_left'
soup = fetch_htmldata(movies_url)
genres = fetch_genres(soup)