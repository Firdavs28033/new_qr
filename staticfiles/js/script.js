"use strict";


function darkmode() {
    const body = document.body
    const wadDarkmode = localStorage.getItem('darkmode') === 'true'

 
    localStorage.setItem('darkmode', !wadDarkmode)
    body.classList.toggle('dark-mode', !wadDarkmode)


}

document.querySelector('.image-button').addEventListener('click', darkmode)


