const burger_btn = document.querySelector('#burger_btn')
const nav_frame = document.querySelector('#nav_frame')
const nav_menu = document.querySelector('#nav_menu')
const close_btn = document.querySelector('#close_btn')

const toggleNav = (e) => {
    nav_menu.classList.toggle('active')
}

burger_btn.addEventListener('click', toggleNav)
nav_frame.addEventListener('click', toggleNav)
close_btn.addEventListener('click', toggleNav)