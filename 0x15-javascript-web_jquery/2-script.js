/*
script Javascript that updates the text color of the HTML tag
header to red (#FF0000) when the user clicks on the tag DIV#red_header
*/
$(document).ready(function () {
  $('#red_header').click(function () {
    $(this).css('color', '#FF0000');
  });
});
