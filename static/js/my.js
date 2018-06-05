$(document).ready(function ($) {
    $('#nav').on('click', '.sub_cat', function(e){
        e.preventDefault();
        var elem = $(this);
        var parent_id = elem.attr('data-patent-id');
        $.ajax({
            url: '/subcategory',
            method: 'POST',
            data: {parent_id: parent_id},
            success: function (responce) {
                elem.closest('li').append(responce);
            }
        });
        console.log(parent_id);
    });
});