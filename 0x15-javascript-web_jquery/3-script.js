// JavaScript using jQuery to add the class 'red' to the header when the div is clicked
$(document).ready(function() {
    $('#red_header').click(function() {
        $('header').addClass('red');
    });
});
