#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
