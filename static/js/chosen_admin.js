$(document).ready(function() {
    $('select').closest('div').removeClass('related-widget-wrapper');
    options = {
      search_contains: true, // plus whatever else you want
    };
    $('select').chosen(options);
});