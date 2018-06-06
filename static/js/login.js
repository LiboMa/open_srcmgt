$(document).ready(function(){

  var msg=$("#msg").text();
  if (msg==null || msg == ""){
    $('#msg').hide();
  }else {
  
    $('#msg').fadeOut(3000);
  
  }


});

//alert("username:"+username+"password:"+ password);

/*if (username ==null || username ==""){
    return false;
};

data="username="+username+"&"+"password="+password
$.ajax({
  type: "POST",
  url: "./login",
  data: data,
//  data:$(".login-form").serialize(),
}).fail(function(){

$("#wmsg").fadeOut("slow")
    // Animation complete.
    //   }); )
//$("#ct2").load("./ori_show");
//$(".nav").load("./ori_show");
});


};


/*if(username.length > 3)
{
$("#status").html('<img src="./static/loader.gif">&nbsp;Checking availability.');

$.ajax({ 
type: "POST", 
url: "check_ajax", 
data: "username="+ username, 
success: function(msg){ 
$("#status").ajaxComplete(function(event, request){ 

if(msg == 'OK')
{ 
// if you don't want background color remove these following two lines
$("#username").removeClass("red"); // remove red color
$("#username").addClass("green"); // add green color
msgbox.html('<img src="./static/yes.png"><font color="Green"> Available </font>');
}else 
{ 
// if you don't want background color remove these following two lines
$("#username").removeClass("green"); // remove green color
$("#username").addClass("red"); // add red  color
msgbox.html(msg);
}
});
}
});

} else
{
$("#username").addClass("red"); // add red color
$("#status").html('<font color="#cc0000">Enter valid User Name</font>')
}

return false;

});*/

