import imdb

ia = imdb.IMDb()

def SearchMovieByName(MovieName):
  Result = {}
  search = ia.search_movie(f"{MovieName}")
  srchrslt = f"{search}"
  srchrslt1 = srchrslt[2:]
  srchrslt2 = srchrslt1[:-3]
  srchrslt3 = str(srchrslt2)
  srchrslt4 = srchrslt3.split("_>, <")
  for i in srchrslt4:
    intialResult = {}
    startid = i.find("Movie id:") + len("Movie id:")
    endid = i.find("[http]")
    movieid = i[startid:endid]
    ttl = i.partition("title:_")[2]
    #Result[str(iid)] = str(ttl)
    series = ia.get_movie(int(movieid))
    intialResult["Title"] = str(ttl)
    intialResult["Title"] = str(series)
    year1=""
    try:
      year2 = series.data['year']
      year1+= f"({year2})"
    except:
      year1+= "(N/A)"
    intialResult["Year"] = str(year1)
    cover2=""
    try:
      cover1 = series.data['cover url']
      cover = f"{cover1}"
      left = '@'
      right = '.jpg'
      lnkt = cover[cover.index(left)+len(left):cover.index(right)]
      old = "@" + f"{lnkt}" + ".jpg"
      mlink = cover.replace(f"{old}", "@.jpg")
      cover2+=f"{mlink}"
    except:
      mlink="https://static10.tgstat.ru/channels/_0/2f/2f9bfb5854cd89d5644304dd58c05298.jpg"
      cover2+=f"{mlink}"
    intialResult["PosterUrl"] = str(cover2)
    Result[str(movieid)] = intialResult
  return Result