
Telegram.WebApp.ready();
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


function NewReleaseFunc(){
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/class')
  .then(function(response) {
    response.text().then(function(data) {
      const Filename = String(data);
      /*window.alert(Filename);*/
      try{
        const fs = require('fs');
        const dir = './' + String(Filename);
        if (fs.existsSync(dir)) {
          window.alert('Directory exists!');
        } else {
          window.alert('Directory not found.');
        }
        /*fetch(Filename)
        .then(response => response.json())
        .then(window.alert(response.responseText))
        .then(data => window.alert(data))
        .catch(error => window.alert(error));
        window.alert("sucess");*/
      }
      catch(err){
        window.alert(err.message);
      }
    });
  });
}


function NewReleaseFuncYyy() {
  const http4 = new XMLHttpRequest();
  http4.open("GET", "https://hdmovie5.herokuapp.com/class");
  http4.send();
  http4.onload = function(){
    var FileAnme = http4.responseText;
    window.alert(FileAnme);
  };//http4.onload = () => 
    //
    
  var request = new XMLHttpRequest();
  request.open('GET', FileAnme, true);
  
  var MovieResult = JSON.parse(request.responseText);
  const el = document.createElement('div');
  
  var x = document.getElementById("NewRelease-Items");
  var y = document.getElementById("NewRelease");
  if (x.style.display === "block") {
    x.style.display = "none";
    y.style.background = "none";
  } else {
    request.onload = function(){ 
    if (request.status >= 200 && request.status < 400) {
      // Success!
      el.innerHTML = MovieResult;
      x.appendChild(el);
    } else {
      // Error//
    }
    x.style.display = "block";
    y.style.background = "rgb(95,95,95)";
  };
  window.alert(http4.responseText);
}}

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

