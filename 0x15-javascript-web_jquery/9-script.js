// JavaScript using jQuery to fetch and display the "hello" translation
$(document).ready(function() {
    // Define the URL to fetch data from
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    
    // Perform the AJAX request
    $.getJSON(url, function(data) {
        // Extract the "hello" value from the response
        var helloTranslation = data.hello;
        
        // Display the "hello" translation in the <div> with ID 'hello'
        $('#hello').text(helloTranslation);
    }).fail(function() {
        // Handle any errors
        $('#hello').text('Failed to fetch hello translation');
    });
});

