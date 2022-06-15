
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

function TopMoviesName() {
  fetch('https://api.codetabs.com/v1/proxy?quest=https://hdmovie5.herokuapp.com/newmovie')
  .then(function(response) {
    response.text().then(function(data) {
      const Filename = JSON.parse(data);
      for (const xy in Filename) {
        const ImageValue = document.createElement('img');
        Newitem.setAttribute('src',String(Filename[String(xy)]));
        var Newitem = document.getElementsByClassName("Slide-Top-Movie");
        window.alert(Filename[String(xy)]);
        /*
        const UrlImage = String(Filename[String(xy)]);
        Newitem.style.background = "url('" + UrlImage + "') top center no-repeat";
        var backgroundStle = "--bg-image: " + String(UrlImage) + ";";
        Newitem.setAttribute('style' , backgroundStle);*/
        /*
        /*const ImageBox = document.createElement('div');
        ImageBox.className = "mySlides-fade";*/
        /*
        ImageValue.setAttribute('height', '30px');
        ImageValue.setAttribute('width', 'auto');
        const CaptionText = document.createElement('div');
        CaptionText.className = "Ctext";
        CaptionText.innerHTML = String(xy);
        ImageBox.appendChild(ImageValue);
        ImageBox.appendChild(CaptionText);
        const UrlImage = 'https://telegra.ph/file/ef2b00a5fcac69ebfe43c.jpg';
        var backgroundStle = "background-image: " + UrlImage + ";";
        ImageBox.setAttribute('style' , backgroundStle);
        var Newitem = document.getElementById("Slide-Top-Movie");
        Newitem.appendChild(ImageBox);
        /*background-image: url('https://telegra.ph/file/4710c1f31d08bd315861c.jpg');
        : cover;
        background-attachment: fixed;*/
        break;
        /*const Text = "<br>Movie Id :" + xy + "<br>Name :"+ Filename[xy];
        window.alert(xy);
        var Newitem = document.getElementById("NewRelease-Items");
        Newitem.appendChild(el);
        window.aler(xy);*/
      }
    });
  });
}

