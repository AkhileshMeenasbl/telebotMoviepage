import requests
from bs4 import BeautifulSoup
import re


def getdata(url):
  r = requests.get(url)
  return r.text
  
def GetAllMovieResult(MovieName):
  print(MovieName)
  movietosearch = f"{MovieName}"
  IMDBURL = f"https://www.imdb.com/find?q={movietosearch}&s=tt&ref_=fn_tt"
  print(IMDBURL)
  Result = {}
  htmldata =  getdata(f"{IMDBURL}")
  soup = BeautifulSoup(htmldata, 'html.parser')
  table_dataResult = soup.find("table")#, attrs={"class":"details"})
  rows = table_dataResult.find_all('tr')
  for i in rows:
    MoVieData = {}
    Imageresult = i.find_all('img')
    Image_Link = str(Imageresult[0]['src'])
    start = '@'
    end = '.jpg'
    lnkt = Image_Link[Image_Link.find(start)+len(start):Image_Link.rfind(end)]
    #lnkt = Image_Link[Image_Link.index(left)+len(left):Image_Link.index(right)]
    Poster = Image_Link.replace(f"{lnkt}", "")
    Titlerwsults = i.find_all('td')
    IMDBid = Titlerwsults[1].find_all('a')[0]['href'].replace("/title/","").replace("/","")
    IMDBname = Titlerwsults[1].text.strip()
    MoVieData["Name"] = str(IMDBname)
    MoVieData["Poster"] = str(Poster)
    Result[str(IMDBid)] = MoVieData
  return Result