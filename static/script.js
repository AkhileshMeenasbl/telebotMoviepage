/*import axios from 'axios';*/

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


function NewReleaseFunchj(){
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/class')
  .then(function(response) {
    response.text().then(function(data) {
      const Filename = String(data);
      /*window.alert(Filename);*/
      try{
        const response = axios.get(Filename);
        const item = response.data;
        window.alert(item);
        /*const fs = require('fs');
        const dir = './' + String(Filename);
        if (fs.existsSync(dir)) {
          window.alert('Directory exists!');
        } else {
          window.alert('Directory not found.');
        }*/
        /*fetch(Filename)
        .then(response => response.json())
        .then(window.alert(response.responseText))
        .then(data => window.alert(data))
        .catch(error => window.alert(error));
        */
        /*$.ajax({
          url: Filename, //the path of the file is replaced by File.json
          dataType: "json",
          success: function (response) {
            console.log(response); //it will return the json array
          }
        });
        window.alert("sucess" + response);*/
        /*var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
        xobj.open('GET', Filename, true); // Replace 'appDataServices' with the path to your file
        xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
            try{
              window.alert(xobj.responseText)}
            catch(err){
            }
          }
        };
        xobj.send(null);*/
      }
      catch(err){
        window.alert(err.message);
      }
    });
  });
}


function NewReleaseFunc() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/class')
  .then(function(response) {
    response.text().then(function(data) {
      const Filename = String(data);
      try{
          fetch(Filename)
          .then(response => response.json())
          .then(json => {
            /*window.alert("akhil");
            const Result = json;
            for (const xy in Result) {
              const el = document.createElement('div');
              const Text = "<br>Movie Id :" + xy + "<br>Name :"+ Result[xy];
              el.innerHTML = String(Text);
              var Newitem = document.getElementById("NewRelease-Items");
              Newitem.appendChild(el);
              */window.alert(x);/*
              console.log(Result[x]);
              }*/
            });
          }
      catch(err){
        window.alert(err.message);
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

