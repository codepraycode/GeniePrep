$(function() {
    //var time = $("#timer").text("00:00");
    //console.log(time);

    // var timeleft = 36000;

    function displayTime(time) {


        var min = Math.floor(time / (60 * 1000));

        var mins = min < 10 ? `0${min}` : `${min}`
            //var sec = Math.floor(countdown - (min * 60 * 1000));  // wrong
        var sec = Math.floor((time - (min * 60 * 1000)) / 1000); //correct
        var secs = sec < 10 ? `0${sec}` : `${sec}`


        $("#timer").html(`${mins}:${secs}`);


    }

    const getCookie = (cookiename) => Cookies.get(cookiename);

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });




    //console.log(getCookie())


    $("#submit").on('click', function(e) {
        var answer_sheet = $("#sheet").serialize();
        console.log(answer_sheet);

        $.ajax({
            type: "POST",
            url: "practise",
            data: answer_sheet,
            //dataType: "json",
            success: function(data) {
                //console.log(data, status);
                console.log("answers Submitted");
                // window.location = "";
            },
            error: function(xhr, errmsg, err) {
                $('#notify').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

    });

    var countdown = 1.25 * 60 * 1000;
    var timerId = setInterval(function() {
        countdown -= 1000;

        if (countdown <= 0) {
            //alert("30 min!");
            clearInterval(timerId);
            //doSomething();
        } else {
            displayTime(countdown); //$("#countTime").html(min + " : " + sec);
        }

    }, 1000); //1000ms. = 1sec




})