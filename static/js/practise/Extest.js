$(function() {
    //var time = $("#timer").text("00:00");
    //console.log(time);

    // var timeleft = 36000;

    function displayTime(time) {
        // time in seconds


        if (time === 0) {
            var mins = "00";
            var secs = "00";
        } else {
            var min = Math.floor(time / (60 * 1000));
            var mins = min < 10 ? `0${min}` : `${min}`
                //var sec = Math.floor(countdown - (min * 60 * 1000));  // wrong
            var sec = Math.floor((time - (min * 60 * 1000)) / 1000); //correct
            var secs = sec < 10 ? `0${sec}` : `${sec}`
        }

        $("#timer").html(`${mins}:${secs}`);



    }


    var duration = $("#timer").data('timer');
    // console.log(duration);
    var countdown = parseFloat(duration) * 60 * 1000;
    var timerId = setInterval(function() {
        countdown -= 1000;

        if (countdown <= 0) {
            countdown = 0
                //alert("30 min!");
            clearInterval(timerId);
            // console.log("Time Up");
            //doSomething();
            $("#submit_test").click();

        }

        displayTime(countdown); //$("#countTime").html(min + " : " + sec);



    }, 1000); //1000ms. = 1sec




})