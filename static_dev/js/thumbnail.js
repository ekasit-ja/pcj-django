var scope = $('.product-section');
var title = scope.find('.product-title');
var image = scope.find('.product.frame img');
var s = 300;

// hide fade-in first
scope.find('.fade-in').fadeOut(0);

scope.find('.thumbnail.frame').click(function(e) {
    var this_ = $(this)
    var img = this_.find('img');

    // must find fade-in fade-out object every click
    var fade_in = scope.find('.fade-in');
    var fade_out = scope.find('.fade-out');

    // change selected item
    scope.find('.selected').removeClass('selected');
    this_.addClass('selected');

    // change title
    title.text(img.data('title'));

    // change fade-in item  to be fade-out
    fade_in.attr('src', img.attr('src'));
    fade_in.fadeIn(s, function() {
        fade_in.removeClass('fade-in').addClass('fade-out').css('z-index', 2);
    });

    // change fade-out item  to be fade-in
    fade_out.fadeOut(s, function() {
        fade_out.attr('src', img.attr('src'));
        fade_out.removeClass('fade-out').addClass('fade-in').css('z-index', 1);
    });
});

// for prev, next control button
scope.find('.control').click(function(e) {
    var this_ = $(this)

    var move = 0;
    if(this_.hasClass('prev')) {
        move = -1;
    }
    else {
        move = 1;
    }

    var selected = scope.find('.selected').find('img')
    var lastIndex = scope.find('[data-last]').data('index')
    var currentIndex = selected.data('index');

    var nextIndex = 0;

    if(move == 1 && currentIndex == lastIndex) {
        nextIndex = 1;
    } else if (move == -1 && currentIndex == 1) {
        nextIndex = lastIndex
    } else {
        nextIndex = currentIndex + move;
    }

    scope.find('[data-index="' + nextIndex +'"]').parent().click();
});
