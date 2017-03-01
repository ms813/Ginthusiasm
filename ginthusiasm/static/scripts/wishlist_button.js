$(document).ready(() => {
    $('.wishlist-button').on('click', e => {
        //the gin slug lives as a data attribute on the wishlist button
        var gin_slug = $(e.target).closest('.wishlist-button').first().data('gin-slug');

        //do the post request, passing the gin slug as a parameter
        var request = $.post('/wishlist/add/', { gin_slug: gin_slug });

        //callback when the post request is successful
        request.done((data, status, jqXHR) => {

            //data is the response from the server
            if(data === 'added'){
                $(e.target).text("Remove from wishlist");
            } else if(data === 'removed'){
                $(e.target).text("Add to wishlist");
            } else {
                //no user logged in, data === 'unauthenticated'
                //redirect to login page
                window.location.replace('/login/');
            }
        });

        //callback if post request fails
        request.fail((data, status, jqXHR) => console.log(data, status, jqXHR));

        //prevent <a> tag from actually redirecting
        return false;
    });
});
