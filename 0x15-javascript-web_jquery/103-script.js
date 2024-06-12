$(document).ready(function () {
    function hello (event) {
      const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
      $.getJSON(url, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
    $('INPUT#btn_translate').on('click', hello);
    $('INPUT#language_code').on('keypress', function (event) {
      const keyy = (event.KeyCode ? event.KeyCode : event.which);
      if (keyy === 13) hello(event);
    });
  })
