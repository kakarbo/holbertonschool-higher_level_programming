/*
script that adds the class red to the HTML tag header
when the user clicks on the DIV#red_header
*/
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
