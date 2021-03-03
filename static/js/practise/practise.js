$(function() {
    // $(".content").load('practise?m=setup');

    /*
    $("#submit_setup").click(function() {
        $("#setup").trigger('submit');
    });*/

    $(".instruction").hide();
    $(".ssetup").show();

    // start button method in setup.js in the ajax call
    $("#back").click(function(e) {
        e.preventDefault();
        $(".instruction").hide();
        $(".ssetup").show();


    });
    //sessionStorage.setItem("controlID", "This is my session");


    const getCookie = (cookiename) => Cookies.get(cookiename);

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });




    //console.log(getCookie())

    // When submit button is clicked
    // During or after test
    $("#submit_test").on('click', function(e) {
        e.preventDefault();
        console.log("Practise Submitted");
        var answer_sheet = $("#sheet").serialize();
        console.log(answer_sheet);

        /*
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
        */
    });

});