var gin_search_url = "/gin/?keywords=";
var distillery_search_url = "/distillery/?distillery_name=";
var destination_url = gin_search_url;

$(document).ready(() => {
    openTab(null, "Gin");

    // if the cursor is in the feature search bar, bind the enter key to search
    $('#feature-search-field').keyup(e => {
        if(e.which === 13){
            featureSearch(e);
        } else {
            autocomplete();
        }
    });
});

// Function to execute the search and request the appropriate search page
var featureSearch = function(e) {
    // grab the string from the search box
    var inputString = $('#feature-search-field').val();

    // remove punctuation and whitespace, replace spaces with +
    var keywords = inputString.replace(/[^\w\s]/g, "").replace(/\s+/g, "+");

    // make a GET request for the search url
    window.location = destination_url + keywords;

    return false;
}

// Function to get the autocomplete results when searching by gin
var gin_autocomplete = function() {
    if ($('#feature-search-field').val().length > 0) {
        var request = $.post('/gin-search/', {
                search_text : $('#feature-search-field').val(),
                csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()
            }
        )

        request.done(function(data, textStatus, jqXHR) {
            $('#feature-search-results').html(data);
        });
    } else {
        $('#feature-search-results').html();
    }
}

// Function to get the autocomplete results when searching by distillery
var distillery_autocomplete = function() {
    if ($('#feature-search-field').val().length) {
        var request = $.post('/distillery-search/', {
                search_text : $('#feature-search-field').val(),
                csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val()
            }
        ).done(function(data, textStatus, jqXHR) {
            $('#feature-search-results').html(data);
        });
    } else {
        $('#feature-search-results').html();
    }
}

// Variable stores the function to complete the autocomplete
var autocomplete = gin_autocomplete;

// Function controls the click behaviour of the tabs 
function openTab(evt, tabName) {
    // Declare all variables
    if (tabName === "Gin") {
        destination_url = gin_search_url;
        $('#Gin.tablinks').css("background-color", "#aaa");
        $('#Distillery.tablinks').css("background-color", $('.tab').css("background-color"));
        autocomplete = gin_autocomplete;
    } else if (tabName === "Distillery") {
        destination_url = distillery_search_url;
        $('#Distillery.tablinks').css("background-color", "#aaa");
        $('#Gin.tablinks').css("background-color", $('.tab').css("background-color"));
        autocomplete = distillery_autocomplete;
    }
}
