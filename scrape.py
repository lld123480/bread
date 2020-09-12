from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import os
import sys



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = 'https://www.seriouseats.com/recipes/2012/08/grilled-butterflied-chicken-recipe.html'

def openJSON(JSONfile):
    with open(JSONfile) as json_file:# arbitrary file name
        data = json.load(json_file)#dict

    json_file.close() 

    return data  

def exportJSON(data,JSONfile):
    with open(JSONfile, 'w') as outfile:
        json.dump(data,outfile)
    outfile.close()

class ScrapeTool(): # 

    def __init__(self,urlsDic):
        self.urlsDic = urlsDic
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    def desoup(self, url):
        req = Request(url=url,headers=self.headers)
        page = urlopen(req)
        soup = BeautifulSoup(page,'html.parser')

        return soup
    
    def recipeScrape(self, soup):
        content = soup.find_all('p')
        article = ""

        for i in content:
            article = article + " " + i.text
        
        return article

    def createDic(self, inputDic):
        newDic = {}
        for keys in inputDic:
            desouped = self.desoup(inputDic[keys])
            scraped = self.recipeScrape(desouped)
            newDic[keys] = scraped
        return newDic


if __name__ == '__main__':
    dataIn = openJSON('data.json')
    recipes = ScrapeTool(dataIn)
    dataOut = recipes.createDic(dataIn)
    exportJSON(dataOut,'Outdata.json')
