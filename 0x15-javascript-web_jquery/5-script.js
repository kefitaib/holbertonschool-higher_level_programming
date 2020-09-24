#!/usr/bin/node
const $ = window.$;
$('DIV#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
