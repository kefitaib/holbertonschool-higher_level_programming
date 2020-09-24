#!/usr/bin/node
const $ = window.$;
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json',
    function (data, textStatus) {
      const res = data.results;
      let s = '';
      for (const x of res) {
        s += x.title + '<br />';
      }
      $('UL#list_movies').html(s);
    });
});
