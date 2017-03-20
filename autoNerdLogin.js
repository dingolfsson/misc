// ==UserScript==
// @name    autoNerdLogin
// @match  *://www.nord.is/*
// @author  Ingolfsson
// @version 1337
// ==/UserScript==

var x = document.getElementById("topBar").querySelectorAll(".innskra-label")[0].innerHTML;

if (x == "Innskráning") {
    (document.getElementsByClassName("style-scope paper-icon-button x-scope iron-icon-0")[1]).click();
    setTimeout(function(){ (document.getElementsByClassName("content  style-scope paper-button x-scope paper-material-0")[1]).click(); }, 1000);
}
