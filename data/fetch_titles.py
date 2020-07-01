# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:40:43 2020

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

def get_titles(soup):
    names = []

    for td in soup.select('table.wikitable.sortable tr td:nth-child(1)'):
        
        title = td.text.strip()
        if len(title) > 2:
            names.append(title)

    return names


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






















