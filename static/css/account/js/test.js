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



// Tabs and it's Contents Javascript Code

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;


    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }


    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";


}

// Sidebar tabs content Javascript Code



function openEach(evt, cityName) {
    // Declare all variables
    var e, tabContent, tabLinks;

    // Get all elements with class="tabcontent" and hide them
    tabContent = document.getElementsByClassName("sidetabcontent");
    for (e = 0; e < tabContent.length; e++) {
        tabContent[e].style.display = "none";
    }




    // Get all elements with class="tablinks" and remove the class "active"
    tabLinks = document.getElementsByClassName("sidetablink");
    for (e = 0; e < tabLinks.length; e++) {
        tabLinks[e].className = tabLinks[e].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}


// Timer Javascript is below the body tag