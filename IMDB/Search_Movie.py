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
    startid = i.find("Movie id:") + len("Movie id:")
    endid = i.find("[http]")
    iid = i[startid:endid]
    ttl = i.partition("title:_")[2]
    Result[str(iid)] = str(ttl)
  return Result