$(document).ready(()=>{
    $('.wishlist-button').on('click', e => {
        var gin_widget = $(e.target).closest('.gin_widget');
        gin_widget.slideUp('slow', () => {
            var wishlistlen= $('#wishlistlen').data('wishlistlen')
            $('#wishlistlen').data('wishlistlen', --wishlistlen);

            if (wishlistlen === 0){
                $('#wishlistlen').text("You have no gins left on your wishlist!").slideDown('slow');
            }
        });
    });
});
