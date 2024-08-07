// JavaScript using jQuery to change the text color of the header when the div is clicked
$(document).ready(function() {
    $('#red_header').click(function() {
        $('header').css('color', '#FF0000');
    });
});
