$(document).ready(function(){                                                                                                              
//  $("tr:odd").css("background-color","rgba(216, 229, 255, 0.2)")
  $("[id=eth2]").hide();
  $("td[id^=td_eth2]").hide();

//focus search box..
/*  $(document).keypress(function(event){
    
    if(event.)
      $('.sbtn').focus();
  });
  
});*/
/*$('.menubtn').click(function(){

    $('.ct1-views').toggle();

});*/
$('a').click(function(){
    
    $('a').removeClass('active');
    $(this).addClass('active');
})


// server status style
$("[id^=td_status]").each(function() {

    switch($.trim($(this).text())) {
        
      case 'online':
            $(this).addClass("green");
            break;
      case 'pending':
            $(this).addClass("yellow");
            break;
      case 'offline':
            $(this).addClass("red");
            break;
      default:
            break;
                 
       }

});

});

