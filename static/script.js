//// MOVIE NEW POSTER CHANGING FUCNTION
var FixedNumberValue = 5; 
var TotlaPicsForNewmOvie = 5;
var picToDisplay = 1;
updateTotalPosters();
//// MOVIE NEW POSTER CHANGING FUCNTION
Telegram.WebApp.ready();
TopMoviesName();

/*MAIN BUTTON CONFIGURE*/
Telegram.WebApp.MainButton.show();
configureMainButton({text: 'requested movie', color: '#008000', onclick: mainButtonClickListener});
function configureMainButton({text, color, textColor = '#ffffff', onclick}) {
    Telegram.WebApp.MainButton.text = text.toUpperCase();
    Telegram.WebApp.MainButton.color = color;
    Telegram.WebApp.MainButton.textColor = textColor;
    Telegram.WebApp.MainButton.onClick(onclick);
}
/*WEB APP THEME*/
configureThemeColor(Telegram.WebApp.colorScheme);
function configureThemeColor(color) {
    if (color === 'dark') {
        document.documentElement.style.setProperty('--body-background-color', '#1f1e1f');
        document.documentElement.style.setProperty('--title-color', 'white');
        document.documentElement.style.setProperty('--sub-text-color', 'white');
    }
}
/*MAIN BUTTON LISTENER*/
function mainButtonClickListener() {
    if (Telegram.WebApp.MainButton.text.toLowerCase() === 'requested movie') {
        configureMainButton({text: 'close', color: '#FF0000', onclick: mainButtonClickListener});
    } else {
        configureMainButton({text: 'requested movie', color: '#008000', onclick: mainButtonClickListener});
    }
    /*cart.classList.toggle('active');*/
}


function NewReleaseFunc() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/class')
  .then(function(response) {
    response.text().then(function(data) {
      const Filename = JSON.parse(data);
      for (const xy in Filename) {
        const el = document.createElement('div');
        const Text = "<br>Movie Id :" + xy + "<br>Name :"+ Filename[xy];
        el.innerHTML = String(Text);
        var Newitem = document.getElementById("NewRelease-Items");
        Newitem.appendChild(el);
        }
      });
    });
  var x = document.getElementById("NewRelease-Items");
  var y = document.getElementById("NewRelease");
  if (x.style.display === "block") {
    x.style.display = "none";
    y.style.background = "none";
  } else {
    x.style.display = "block";
    y.style.background = "rgb(95,95,95)";
  }
}

function TrendingFunc() {
  var x = document.getElementById("Trending-Items");
  var y = document.getElementById("Trending");
  if (x.style.display === "block") {
    x.style.display = "none";
    y.style.background = "none";
  } else {
    x.style.display = "block";
    y.style.background = "rgb(95,95,95)";
  }
}
/// FUNCTION OF MOVIE CHANGING AT INTERVAL 
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
          TitleName.innerHTML = String(TitleNameofMovie);
          var ImageValue = document.getElementById("ImagValues");
          ImageValue.setAttribute('src',MoviePageUrl);
        }
      }
    });
  });
}

function updateTotalPosters() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/newmovie')
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
  ///updateTotalPosters();
  UpdateTimes();
  GetPicNumber();
  TopMoviesName();
  console.log("akhil")
}, 3000);
/// FUNCTION OF MOVIE CHANGING AT INTERVAL 

