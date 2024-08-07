// JavaScript using jQuery to fetch and display the character name
$(document).ready(function() {
    // Define the URL
    var url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    
    // Perform the AJAX request
    $.getJSON(url, function(data) {
        // Extract the character name from the response
        var characterName = data.name;
        
        // Display the character name in the <div> with ID 'character'
        $('#character').text(characterName);
    }).fail(function() {
        // Handle any errors
        $('#character').text('Failed to fetch character name');
    });
});
