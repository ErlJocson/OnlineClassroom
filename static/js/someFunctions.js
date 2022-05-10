function sideNavigationBar(id) {
  var navBurger = document.getElementById(id);
  if (navBurger.style.display === "none") {
    navBurger.style.display = "flex";
  } else {
    navBurger.style.display = "none";
  }
}

function showAnotherDiv(id) {
  var navBurger = document.getElementById(id);
  navBurger.style.display = "none";
}
