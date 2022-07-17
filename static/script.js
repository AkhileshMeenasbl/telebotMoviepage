//// MOVIE NEW POSTER CHANGING FUCNTION
var FixedNumberValue = 5; 
var TotlaPicsForNewmOvie = 5;
var picToDisplay = 1;
updateTotalPosters();
TopMoviesName();

function TopMoviesName() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/newmovie')
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
