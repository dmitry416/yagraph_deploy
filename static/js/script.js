var len;
var arr = [];
var arrhist = [];

mainFunc = function() {
if (arrhist.length == 0) {
  $.get("/gethistory", function(data) {
    arrhist = $.parseJSON(data)
});
}

  jQuery('#all-points').on('change', function(){
    len = jQuery('#all-points').val();
    if (len > 30) {
    len = 30;
    jQuery('#all-points').val(len);
    }
    arr = []
    var table = `<table class="table"><tr>`;
    for (var i = 0; i <= len; i++){
      if (i != 0) {
        table += `</tr>`;
        arr[i - 1] = [];
      }
    for (var j = 0; j <= len; j++){
        if (i == 0) {
          if (j != 0) {
            table += `<td><div class="table-index">${j - 1}</div></td>`;
          }
          else {
            table += `<td><div class="table-index"> </div></td>`
          }
        }
        else if (j == 0) {
          table += `<td><div class="table-index">${i - 1}</div></td>`;
        }
        else {
          arr[i - 1][j - 1] = 0;
          table += `<td><input type="number" value="0" id="id${i - 1}-${j - 1}" class="cell"></td>`;
      }
}}
    table += `</table>`;
    jQuery('table').remove();
    jQuery('.div-table').append(table);
    mainFunc();
  });

  jQuery('.cell').on('change', function(){
    var id = $(this).attr('id');
    var tire = id.indexOf("-");
    arr[Number(id.slice(2, tire))][Number(id.slice(tire + 1, id.length))] = Number($(this).val());
  });

  $('.open-popup').click(function(e) {
    e.preventDefault();
    $('.popup-bg').fadeIn(800);
    $('html').addClass('no-scroll');
});

$('.alg').click(function(e) {
    e.preventDefault();
    $('.popup-out-bg').fadeIn(800);
    $('html').addClass('no-scroll');
});

  $('.popup-bg').click(function() {
    $('.popup-bg').fadeOut(800);
    $('html').removeClass('no-scroll');
});

$('.popup-out-bg').click(function() {
    $('.popup-out-bg').fadeOut(800);
    $('html').removeClass('no-scroll');
});

jQuery('#save').on('click', function(){
  arrhist = JSON.parse(JSON.stringify(arr));
  $.post( "/save", {
    javascript_data: JSON.stringify(arr)
});
});

jQuery('#bfs').on('click', function(){
  $.post( "/bfs", {
    javascript_data: JSON.stringify(arr)
});

$.get("/bfs", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});

jQuery('#dj').on('click', function(){
  $.post( "/dj", {
    javascript_data: JSON.stringify(arr)
});

$.get("/dj", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});

jQuery('#ham').on('click', function(){
  $.post( "/ham", {
    javascript_data: JSON.stringify(arr)
});

$.get("/ham", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});

jQuery('#eul').on('click', function(){
  $.post( "/eul", {
    javascript_data: JSON.stringify(arr)
});

$.get("/eul", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});

jQuery('#tree').on('click', function(){
  $.post( "/tree", {
    javascript_data: JSON.stringify(arr)
});

$.get("/tree", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});


jQuery('#min-tree').on('click', function(){
  $.post( "/mintree", {
    javascript_data: JSON.stringify(arr)
});

$.get("/mintree", function(data) {
    console.log(data);
    jQuery('textarea').remove();
    jQuery('.menu-form-out').append(`<textarea readonly>${String(data)}</textarea>`);
});
});


jQuery('#load').on('click', function(){
  if (arrhist.length == 0) {
  $.get("/gethistory", function(data) {
    arrhist = $.parseJSON(data)
});
}
    arr = JSON.parse(JSON.stringify(arrhist));

  len = arr.length;
  jQuery('#all-points').val(len);
  var table = `<table class="table"><tr>`;
  for (var i = 0; i <= len; i++){
    if (i != 0) {
      table += `</tr>`;
    }
  for (var j = 0; j <= len; j++){
      if (i == 0) {
        if (j != 0) {
          table += `<td><div class="table-index">${j}</div></td>`;
        }
        else {
          table += `<td><div class="table-index"> </div></td>`
        }
      }
      else if (j == 0) {
        table += `<td><div class="table-index">${i}</div></td>`;
      }
      else {
        table += `<td><input type="number" value="${arr[i - 1][j - 1]}" id="id${i - 1}-${j - 1}" class="cell"></td>`;
    }
}}
  table += `</table>`;
  jQuery('table').remove();
  jQuery('.div-table').append(table);
  mainFunc();
});


}



jQuery('document').ready(mainFunc);
