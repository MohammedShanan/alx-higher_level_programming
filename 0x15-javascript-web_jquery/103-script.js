$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keydown(function (event) {
    if (event.key === 'Enter') {
      translate();
    }
  });
  function translate () {
    $.get(
      url + $.param({ lang: $('INPUT#language_code').val() }),
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  }
});
