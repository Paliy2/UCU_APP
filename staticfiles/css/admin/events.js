$('input[name="completed"]').click(function(){
  data['checked'] = $(this).value()
  data['todo_title'] =  $(this).text()
  $.ajax({
    url: 'path/to/save_state',
    type: 'POST',
    data: data
  });
});