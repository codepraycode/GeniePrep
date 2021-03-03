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