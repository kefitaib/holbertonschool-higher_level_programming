#!/usr/bin/node
const $ = window.$;
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
});
