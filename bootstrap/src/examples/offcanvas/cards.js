
$(document).ready(function () {
  $(".card-type").click(function () {
    console.log($(this).parent().find('.card-name').text())
  });
});
