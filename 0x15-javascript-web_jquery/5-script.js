// JavaScript using jQuery to add a new <li> element to the list when the div is clicked
$(document).ready(function() {
    $('#add_item').click(function() {
        $('.my_list').append('<li>Item</li>');
    });
});
