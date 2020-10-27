$('#language-list a').on('click', function (event) {
    event.preventDefault();
    var target = $(event.target);
    var url = target.attr('href');
    var language_code = target.data('language-code');
    $.ajax({
      type: 'POST',
      url: url,
      data: { language: language_code },
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    }).done(function (data, textStatus, jqXHR) {
      reload_page();
    });
  });

  function getCookie(name) {
    var value = '; ' + document.cookie,
      parts = value.split('; ' + name + '=');
    if (parts.length == 2) return parts.pop().split(';').shift();
  }

  function reload_page() {
    window.location.reload(true);
  }