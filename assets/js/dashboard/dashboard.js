$(document).ready(function() {
    $("#dashy").show();
    $("#content").hide();

    $("#dash-btn").on('click', function(e) {
        e.preventDefault();
        $("#dashy").show();
        //console.log("Yes, I caught that event");
        $("#content").hide();
        //console.log("Something had happened");
    });

    $("#profile-btn").on('click', function(e) {
        e.preventDefault();
        $("#dashy").hide();
        $("#content").show();
        //console.log("Yes, I caught that event");
        $("#content").load('profile');
        //console.log("Something had happened");
    });


    $("#target-btn").on('click', function(e) {
        e.preventDefault();
        $("#dashy").hide();
        $("#content").show();
        //console.log("Yes, I caught that event");
        $("#content").load('targets');
        //console.log("Something had happened");
    });

    $("#record-btn").on('click', function(e) {
        e.preventDefault();
        $("#dashy").hide();
        $("#content").show();
        //console.log("Yes, I caught that event");
        $("#content").load('records');
        //console.log("Something had happened");
    });

    $("#leaderboard-btn").on('click', function(e) {
        e.preventDefault();
        $("#dashy").hide();
        $("#content").show();
        console.log("Yes, I caught that event");
        $("#content").load('leaderboard');
        //console.log("Something had happened");
    });
});