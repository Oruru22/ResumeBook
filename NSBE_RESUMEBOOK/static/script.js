const navbar = document.querySelector(".navbar");

const navbarOffset = navbar.offsetTop;

function makeNavbarSticky() {
    if (window.pageYOffset >= navbarOffset) {
        navbar.classList.add("sticky");
    } 
    else {
        navbar.classList.remove("sticky");
    } 
}

window.addEventListener("scroll", makeNavbarSticky);