//My Preloader Code
var loader;

function loadNow(opacity) {
    if (opacity <= 0) {
        displayContent();
    } else {
        loader.style.opacity = opacity;
        window.setTimeout(function() {
            loadNow(opacity - 0.05);
        }, 50);
    }
}

function displayContent() {
    loader.style.display = 'none';
    document.getElementById('content').style.display = 'block';
}

document.addEventListener("DOMContentLoaded", function() {
    loader = document.getElementById('loading-icon-bx');
    loadNow(1);
});
// End Of Preloader


const body = document.body;
const menuLinks = document.querySelectorAll(".admin-menu a");
const collapseBtn = document.querySelector(".admin-menu .collapse-btn");
const toggleMobileMenu = document.querySelector(".toggle-mob-menu");
const collapsedClass = "collapsed";

collapseBtn.addEventListener("click", function() {
    this.getAttribute("aria-expanded") == "true" ?
        this.setAttribute("aria-expanded", "false") :
        this.setAttribute("aria-expanded", "true");
    this.getAttribute("aria-label") == "collapse menu" ?
        this.setAttribute("aria-label", "expand menu") :
        this.setAttribute("aria-label", "collapse menu");
    body.classList.toggle(collapsedClass);
});

toggleMobileMenu.addEventListener("click", function() {
    this.getAttribute("aria-expanded") == "true" ?
        this.setAttribute("aria-expanded", "false") :
        this.setAttribute("aria-expanded", "true");
    this.getAttribute("aria-label") == "open menu" ?
        this.setAttribute("aria-label", "close menu") :
        this.setAttribute("aria-label", "open menu");
    body.classList.toggle("mob-menu-opened");
});

for (const link of menuLinks) {
    link.addEventListener("mouseenter", function() {
        body.classList.contains(collapsedClass) &&
            window.matchMedia("(min-width: 768px)").matches ?
            this.setAttribute("title", this.textContent) :
            this.removeAttribute("title");
    });
}