$(document).ready(function(){

  console.log('im working');

  $('input').focus(function(){
    $(this).parent().find(".label-txt").addClass('label-active');
  });

  $("input").focusout(function(){
    if ($(this).val() == '') {
      $(this).parent().find(".label-txt").removeClass('label-active');
    };
  });




  // $('a#upvote').bind('click', function() {
  //   // alert('like clicked');
  //   $.getJSON('/like',
  //     function(data) {
  //       //do nothing
  //     });
  //   return false;
  // });


});

// document.getElementById('upvote').addEventListener(
//   'click', loadText);


function loadText(){
  alert('Button clicked');
}
