$(function() {

    //Select all Subjects
    $("#of_all_subject").click(function() {
        $("#subj1").trigger('click');
        $("#subj2").trigger('click');
        $("#subj3").trigger('click');
        $("#subj4").trigger('click');
    });

    // Subject 1
    $("#subj1_from").prop('disabled', true)
    $("#subj1_to").prop('disabled', true);

    $("#subj1").click(function() {
        if ($(this).is(':checked')) {
            $("#subj1_from").prop('disabled', false)
            $("#subj1_to").prop('disabled', false);
        } else {
            $("#subj1_from").prop('disabled', true)
            $("#subj1_to").prop('disabled', true);
        }


    });

    // Subject 2
    $("#subj2_from").prop('disabled', true)
    $("#subj2_to").prop('disabled', true);

    $("#subj2").click(function() {
        if ($(this).is(':checked')) {
            $("#subj2_from").prop('disabled', false)
            $("#subj2_to").prop('disabled', false);
        } else {
            $("#subj2_from").prop('disabled', true)
            $("#subj2_to").prop('disabled', true);
        }


    });

    // Subject 3
    $("#subj3_from").prop('disabled', true)
    $("#subj3_to").prop('disabled', true);

    $("#subj3").click(function() {
        if ($(this).is(':checked')) {
            $("#subj3_from").prop('disabled', false)
            $("#subj3_to").prop('disabled', false);
        } else {
            $("#subj3_from").prop('disabled', true)
            $("#subj3_to").prop('disabled', true);
        }


    });

    // Subject 4
    $("#subj4_from").prop('disabled', true)
    $("#subj4_to").prop('disabled', true);

    $("#subj4").click(function() {
        if ($(this).is(':checked')) {
            $("#subj4_from").prop('disabled', false)
            $("#subj4_to").prop('disabled', false);
        } else {
            $("#subj4_from").prop('disabled', true)
            $("#subj4_to").prop('disabled', true);
        }


    });



    function ParseTime(time) {
        // A function to get time in
        // time -> 00:00
        // An live display the response

        var min_sec, min, sec;
        min_sec = time.split(":");

        min = parseInt(min_sec[0])
        sec = parseInt(min_sec[1])
            //console.log(min, sec)

        minute = min > 1 ? min.toString() + ' minutes' : min.toString() + ' minute';
        second = sec > 1 ? sec.toString() + ' seconds' : sec.toString() + ' second';



        return `${minute}, ${second}`

    }


    function ParseToColon(digit) {
        // Parse the duration from float minutes
        // to minute in this format 00:00
        var fine_duration_in_secs = parseFloat(digit) * 60;
        var fine_duration_min = parseInt(Math.floor(fine_duration_in_secs / 60));
        var fine_duration_sec = parseInt(fine_duration_in_secs % 60);

        var final_fine_duration = `${fine_duration_min}:${fine_duration_sec}`;
        //console.log(final_fine_duration);
        return final_fine_duration;
    }


    // Time Picking
    $('.clockpicker').clockpicker()
        .find('input').change(function() {
            // TODO: time changed
            var vale = this.value.slice(0, 5);
            $(this).val(vale);
            console.log(vale);
            //console.log($("#timeParse").text());
            //ParseTime(vale);
            $("#timeParse").text(ParseTime(vale));

        });

    /*
    $('#demo-input').clockpicker({
        autoclose: true
    });*/

    /*
        if (something) {
            // Manual operations (after clockpicker is initialized).
            $('#demo-input').clockpicker('show') // Or hide, remove ...
                .clockpicker('toggleView', 'minutes');
        }
    */


    // Setup Submission
    // When setup Form submits
    $("#setup").submit(function(e) {
        e.preventDefault();
        e.stopPropagation();


        var datar = $(this).serialize();

        ////
        /*
        var setup_data = $(this).serialize().split("&");
        // console.log(setup_data);
        var obj = {};
        for (var key in setup_data) {
            // console.log(setup_data[key]);
            var k = setup_data[key].split("=")[0]
            var v = setup_data[key].split("=")[1]

            obj[k] = v;
        }*/

        //console.log(typeof(obj));


        var subjects; // A list of Json of subjects data
        // used in and after ajax call
        var duration; // Duration of test
        // seted after ajax call

        // Make a the setup
        $.ajax({
            // Make a Ajax setup API
            url: "practise?m=setup",
            data: datar,

            success: function(data) {
                //console.log("It went well");
                // console.log(data);

                if (data.good) {
                    var prep_subjects = ''; // Prepare subjects
                    var questions = '';
                    var question_range; // Question range

                    duration = data.duration // set the duration
                    var fine_duration = ParseToColon(duration);

                    subjects = data.subjects; // A list of Json
                    // var quest_range;

                    // Subjects is an Array -> [{name, start, stop}]
                    //console.log(subjects);

                    // Iterate through the subjects
                    subjects.forEach(obj => {
                        // console.log(obj.name);
                        prep_subjects += obj.name + ', '
                            // console.log(obj.start);
                            //console.log(obj.stop);

                        question_range = obj.quest_range;
                        //question_diff = parseInt(obj.stop) <= 10 ? question_diff + 0 : question_diff + 1;
                        questions += `${question_range} (${obj.start} to ${obj.stop}), `
                    });

                    console.log(`Subjects => ${prep_subjects}`);
                    console.log(`Questions => ${questions}`);
                    console.log(`Time Duration => ${duration} mins`);

                    $(".ssetup").hide();
                    $(".instruction").show();

                    $(".subject_tag").text(prep_subjects);
                    $(".quest_tag").text(questions);

                    $(".timer_tag").text(ParseTime(fine_duration));
                    //console.log($(".subject_tag").text());

                };

            },

            error: function(errmsg) {
                //console.log(xhr.status + ": " + xhr.responseText);;
                console.log(errmsg);
            }
        });

        $("#start").click(function(e) {
            console.log(subjects);
            Cookies.remove('testData');
            Cookies.set('testData', JSON.stringify(subjects));
            //sessionStorage.setItem('testData', JSON.stringify(subjects));
            console.log("Start Practise");
            $("#page").load(`test?dur=${duration}`);
            //window.location = "test";
        });
    });

});