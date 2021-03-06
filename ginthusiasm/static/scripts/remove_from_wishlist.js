$(document).ready(()=>{
    $('.wishlist-button').on('click', e => {
        var gin_widget = $(e.target).closest('.gin_widget').first();
        var gin_slug = $(e.target).closest('.wishlist-button').first().data('gin-slug');
        var gin_name = $(e.target).closest('.wishlist-button').first().data('gin-name');

        gin_widget.slideUp('slow', () => {
            var wishlistlen= $('#wishlistlen').data('wishlistlen');
            $('#wishlistlen').data('wishlistlen', --wishlistlen);

            var back_link = $("<a>", {
                href : "/gin/" + gin_slug + "/",
                text : gin_name
            });
            gin_widget.html("You just removed&nbsp;"+ back_link.prop('outerHTML') + "&nbsp;from your wishlist");

            gin_widget.slideDown('slow');

            if (wishlistlen === 0){
                $('#wishlistlen').html("<strong class='indent'>You have no gins left on your wishlist!</strong>").slideDown('slow');
            }
        });
    });
});
