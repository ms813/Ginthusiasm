$(document).ready(() => {
    $('.wishlist-button').on('click', e => {
        var gin_slug = $(e.target).data('gin');

        var request = $.post('/wishlist/add/' + gin_slug + '/', (data, status, jqXHR) => {
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

        request.fail((data, status, jqXHR) => console.log(data, status, jqXHR));

        //prevent <a> tag from actually redirecting
        return false;
    });
});
