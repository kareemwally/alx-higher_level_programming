// JavaScript using jQuery to fetch and list movie titles
$(document).ready(function() {
    // Define the URL to fetch movie data
    var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    
    // Perform the AJAX request
    $.getJSON(url, function(data) {
        // Extract the list of films from the response
        var films = data.results;
        
        // Create a variable to store the list items
        var listItems = '';
        
        // Iterate over each film and create a list item for each
        $.each(films, function(index, film) {
            listItems += '<li>' + film.title + '</li>';
        });
        
        // Update the content of the <ul> with ID 'list_movies'
        $('#list_movies').html(listItems);
    }).fail(function() {
        // Handle any errors
        $('#list_movies').html('<li>Failed to fetch movie titles</li>');
    });
});
