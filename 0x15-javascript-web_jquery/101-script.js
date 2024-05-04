$(document).ready(function () {
  $('DIV#add_item').click(function (e) {
    e.preventDefault();
    $('.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function (e) {
    e.preventDefault();
    $('.my_list li:last').remove();
  });

  $('DIV#clear_list').click(function (e) {
    e.preventDefault();
    $('.my_list').empty();
  });
});
