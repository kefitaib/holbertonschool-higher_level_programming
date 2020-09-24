const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    $.get(url + $('INPUT#language_code').val(), function (data, statuscode) {
      $('DIV#hello').html(data.hello);
    });
  });
});
