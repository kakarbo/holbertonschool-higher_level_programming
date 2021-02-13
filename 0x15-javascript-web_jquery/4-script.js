/*
Script that toggles the class of the HTML tag header when
the user clicks on the tag DIV#toggle_header
*/
$(document).ready(function () {
  $('#toggle_header').click(function () {
    if($('header').hasClass('green'))
      $('header').removeClass('green');
    $('header').addClass('red');
  });
});
