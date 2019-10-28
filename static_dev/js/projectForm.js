var _page = $("#page");
_page.change(function(e) {
    var country = $('select[name=country]').val()
    var year = $('select[name=year]').val()
    var page = $('select[name=page]').val()

    var url = window.location.origin + window.location.pathname
    url += "?country=" + country + "&year=" + year + "&page=" + page;

    window.location.href = url;
});
