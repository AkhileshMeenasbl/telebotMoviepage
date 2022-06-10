Telegram.WebApp.ready()
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
  var x = document.getElementById("NewRelease-Items");
  var y = document.getElementById("NewRelease");
  if (x.style.display === "block") {
    x.style.display = "none";
    y.style.background = "none";
  } else {
    x.style.display = "block";
    y.style.background = "rgb(95,95,95)";
  }
  let UrlFetch = fetch("https://hdmovie5.herokuapp.com/class");
  UrlFetch.then(response => response.json())
  .then(formatedResponse =>  console.log(formatedResponse));
}

const Newrsult = document.getElementById("NewRelease-Items");

function getDocumentTranslatedText() {
  UrlFetch.then(reetu => {
    document.body.innerHTML;
    const el = document.createElement('div');
    el.innerHTML = reetu;
    Newrsult.appendChild(el);
  });
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

