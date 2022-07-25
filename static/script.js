//// MOVIE NEW POSTER CHANGING FUCNTION
var FixedNumberValue = 5; 
var TotlaPicsForNewmOvie = 5;
var picToDisplay = 1;
updateTotalPosters();
TopMoviesName();

function TopMoviesName() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/newmovieslideposter')
  .then(function(response) {
    response.text().then(function(data) {
      const Result = JSON.parse(data);
      for (const xy in Result) {
        var TitleNameofMovie6 = Result[String(picToDisplay)];
        for (const TitleNameofMovie in TitleNameofMovie6) {
          var MoviePageUrl = String(TitleNameofMovie6[TitleNameofMovie]);
          var TitleName = document.getElementById("TitleOfmovie");
          var ImageValue = document.getElementById("ImagValues");
          var NewMovieSlidBackground = document.getElementById("slideshow-containerid");
          NewMovieSlidBackground.style.backgroundImage = "url('" +  MoviePageUrl + "')";
          ImageValue.setAttribute('src',MoviePageUrl);
          TitleName.innerHTML = String(TitleNameofMovie);
        }
      }
    });
  });
}

function updateTotalPosters() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/newmovieslideposter')
  .then(function(response) {
    response.text().then(function(data) {
      const Result = JSON.parse(data);
     shareInfoLen = Object.keys(Result).length;
     window["FixedNumberValue"] = shareInfoLen;
     window["TotlaPicsForNewmOvie"] = shareInfoLen;
    });
  });
}

function UpdateTimes() {
  var FixedNumberValue1 = FixedNumberValue + 1;
  window["FixedNumberValue"] = FixedNumberValue1;
  }

function GetPicNumber(){
  var RestNum = FixedNumberValue%TotlaPicsForNewmOvie;
  window["picToDisplay"] = Number(RestNum);
}

window.setInterval(function(){
  UpdateTimes();
  GetPicNumber();
  TopMoviesName();
}, 3000);

window.setInterval(function(){
  updateTotalPosters();
}, 192929);
 
//// MOVIE NEW POSTER CHANGING FUCNTION

//// MOVIE SEARCH RESULT IMDB
function SearchMovieByNames() {
  const MovieName = document.getElementById('SearchBar');
  if(String(MovieName.value.replace(/^\s+|\s+$/g,"").length) == 0){
    window.alert("Please Input Movie Name");
  } else {
    const MovieByNameURL = "https://hdmovie5.herokuapp.com/searchmoviebyname?movie_name=";
    var MovieName4search = String(MovieName.value);
    const url2fetch = `${MovieByNameURL}${MovieName4search}`;
    var Moviesearchurl = `https://api.codetabs.com/v1/proxy/?quest=${url2fetch}`;
    var SearchBoxAreaTitle = document.getElementById('SearchBoxTitle');
    SearchBoxAreaTitle.innerHTML = `SEARCH RESULT`;
    var SearchBoxAreaResult = document.getElementById('SearchBoxResult');
    SearchBoxAreaResult.innerHTML = "";
    fetch(Moviesearchurl)
    .then(function(response) {
      response.text().then(function(data) {
        const Result = JSON.parse(data);
        for (const xy in Result) {
          var Movie_Id = xy;
          var Movie_Name = Result[xy]["Name"];
          var MoviePosterURL = Result[xy]["Poster"];
          
          //Function to make new another search result//
          const SearchMovieResult = document.createElement("div");
          SearchMovieResult.className = "SearchMovieResult";
          
          var SMoviePoster = document.createElement('img');
          SMoviePoster.className = "SearchMoviePoster";
          SMoviePoster.src = `${MoviePosterURL}`
          
          var FigCaption = document.createElement('FigCaption');
          FigCaption.className = "FigCaption";
          var smovietitlename = document.createElement('div');
          smovietitlename.innerHTML = `${Movie_Name}`
          var RequestMovieButton = document.createElement('button');
          RequestMovieButton.className = "RequestMovieButton";
          RequestMovieButton.id = `${Movie_Id}`;
          RequestMovieButton.addEventListener("click",SendRequstMovieData);
          RequestMovieButton.innerHTML = "📂 REQUEST"
          
          FigCaption.appendChild(smovietitlename)
          FigCaption.appendChild(RequestMovieButton)
          SearchMovieResult.appendChild(SMoviePoster);
          SearchMovieResult.appendChild(FigCaption);
          SearchBoxAreaResult.appendChild(SearchMovieResult);
        }
      });
    })
    .catch(err => console.log(err));
  }
}
//// MOVIE SEARCH RESULT IMDB
//// MOVIE REUEST FUNCTION
function SendRequstMovieData(evt){
  const Data = evt.target;
  var Movie_id = Data.id;
  fetch('/Submit-Request-for-Movie', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      Movie_id : Movie_id,
      initData : window.Telegram.WebApp.initData
    })
  });
}
//// MOVIE REUEST FUNCTION