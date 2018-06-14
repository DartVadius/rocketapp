jQuery(document).ready(function ($) {

    // hide messages
    $("#error").hide();
    $("#sent-form-msg").hide();

    // on submit...
    $("#contactForm #submit").click(function () {
        $("#error").hide();

        //required:

        //name
        var name = $("input#name").val();
        if (name == "") {
            $("#error").fadeIn().text("Name required.");
            $("input#name").focus();
            return false;
        }

        // email
        var email = $("input#email").val();
        if (email == "") {
            $("#error").fadeIn().text("Email required");
            $("input#email").focus();
            return false;
        }

        // web
        // var web = $("input#web").val();
        // if(web == ""){
        // 	$("#error").fadeIn().text("Web required");
        // 	$("input#web").focus();
        // 	return false;
        // }

        // comments
        var comments = $("#comments").val();

        // send mail php
        var sendMailUrl = $("#sendMailUrl").val();

        // ajax
        $.ajax({
            type: "POST",
            url: sendMailUrl,
            data: {
                'name': name,
                'email': email,
                'comment': comments,
                'csrfmiddlewaretoken': Cookies.get('csrftoken')
            },
            success: success()
        });
    });


    // on success...
    function success() {
        $("#sent-form-msg").fadeIn();
        $("#contactForm").fadeOut();
    }

    return false;
});

