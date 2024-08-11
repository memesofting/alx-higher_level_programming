/* global $ */
$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Fetch translation when ENTER is pressed
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the ENTER key code
      fetchTranslation();
    }
  });
});
