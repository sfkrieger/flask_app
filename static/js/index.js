$(document).ready(function () {
    var $overlay = $('.row');
    $overlay.hover(function () {
        var thisOverlay = $(this).find('.overlay');
        var $overlays = $('.overlay');
        $overlays.finish();
        $overlays.each(function (o) {
            o = $($overlays[o]);
            if (o != thisOverlay) {
                o.css('opacity', 0.3);
            }
        });
        thisOverlay.css('opacity', 0.0);
    });
    $('#all-posts').hover(undefined, function () {
        var $overlays = $('.overlay');
        $overlays.finish();
        $overlays.css('opacity', 0.0);
    });
});