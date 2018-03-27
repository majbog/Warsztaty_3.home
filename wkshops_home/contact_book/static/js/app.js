$(function() {

    console.log("!!");

    var btns = $(".contact-header");

    btns.each(function (i, e) {
        $(this).click(function () {
            $(this).next(".contact-details").toggleClass("hidden");
        });
    });

});