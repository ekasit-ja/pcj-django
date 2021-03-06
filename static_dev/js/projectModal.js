$('.card-project').click(function(e) {
    e.preventDefault();

    var this_ = $(this);
    $.get(this_.attr('href'), function(data) {
        $('#modalTitle').text(data.title);
        $('#modalImg').attr('src', data.image);
        $('#modalAddress').text(data.area + ', ' + data.country);
        $('#modalCompany').text(data.company ? data.company:data.title);
        $('#modalYear').text(data.year);
    });
});
