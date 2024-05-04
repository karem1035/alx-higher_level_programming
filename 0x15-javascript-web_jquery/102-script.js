$(document).ready(function () {
  $('INPUT#btn_translate').click(function (e) {
    e.preventDefault();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${$(
      'INPUT#language_code'
    ).val()}`;

    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
