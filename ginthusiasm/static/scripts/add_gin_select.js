$(document).ready(() => {
    let select = $('#distillery-select');
    // get the selected distillery from the drop down
    // and change the url of the add-gin button
    select.change((e) => {
        let v = $(e.target).val();
        $('#add-gin-btn').attr('href', "/distillery/" + v + "/add-gin/");
    });

    // this prevents the link being followed immediately
    select.on('click', (e) => {
        return false;
    });
});

