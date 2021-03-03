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




    // Time Picking
    $('.clockpicker').clockpicker()
        .find('input').change(function() {
            // TODO: time changed
            var vale = this.value;
            $(this).val(vale.slice(0, 5));
            console.log(this.value);
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
        }*/
});