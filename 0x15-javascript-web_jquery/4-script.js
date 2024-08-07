// JavaScript using jQuery to toggle the class of the header between 'red' and 'green'
$(document).ready(function() {
    $('#toggle_header').click(function() {
        var header = $('header');
        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else {
            header.removeClass('green').addClass('red');
        }
    });
});
