# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:40:43 2020

@author: Daniel Brunnsåker
"""

from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

def extract_integers(value):
    return int(''.join(re.findall('\d+',value)))

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


def get_titles(soup):
    names = []

    for td in soup.select('table.wikitable.sortable tr td:nth-child(1)'):
        
        title = td.text.strip()
        if len(title) > 2:
            names.append(title)

    return names


movies_url = 'https://www.rottentomatoes.com/m/you_should_have_left'
soup = fetch_htmldata(movies_url)
genres = fetch_genres(soup)

list_of_titles = []

for year in range(2000,2019,1):
    print(year)
    list_url = 'https://en.wikipedia.org/wiki/'+str(year)+'_in_film'
    soup = fetch_htmldata(list_url)

    list_of_titles.append(get_titles(soup))

titles = [item for sublist in list_of_titles for item in sublist]
printout = pd.DataFrame(titles)
printout.columns = ['Title']
printout = printout.drop_duplicates()
printout.to_csv('movie_titles.txt', index = False)






















