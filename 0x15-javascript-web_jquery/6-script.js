// JavaScript using jQuery to update the text of the header when the div is clicked
$(document).ready(function() {
    $('#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});
