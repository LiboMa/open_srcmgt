$(document).ready(function(){

var check_status='<span id="status"></span>';
$("#hostname").after(check_status);

/*for (i=0;i<check_items.length;i++){

    check_fuction(check_item[i]);
}*/
var eid='hostname';

$("#"+eid).change(function(){
  var hostname =$("#"+eid).val();
  var msgbox = $("#status");

  if(eid.length > 3)
  {
    $("#status").html('<img src="./static/imgs/loader.gif">&nbsp;Checking availability.');

    $.ajax({ 
    type: "POST", 
    url: "check_host", 
    data: "hostname=" + hostname, 
    success: function(msg){ 
    $("#status").ajaxComplete(function(event, request){ 

        if( msg == 'OK')
        { 
        // if you don't want background color remove these following two lines
        $("#"+ eid).removeClass("red"); // remove red color
        $("#"+ eid).addClass("green"); // add green color
        msgbox.html('<img src="./static/imgs/yes.png"><font color="Green"> Available </font>');
        } else {
        // if you don't want background color remove these following two lines
        $("#"+ eid).removeClass("green"); // remove green color
        $("#" + eid).addClass("red"); // add red  color
        msgbox.html(msg);
           }
      });
     }
    });

  } else
  {
  $("#"+ eid).addClass("red"); // add red color
  $("#status").html('<font color="#cc0000"> Invalid hostname</font>')
  }

  return false;
});

$("#new_save").click(function(){

  check_items=['hostname', 'eth0', 'eth1', 'gateway', 'project']

  $("#status2").remove();
  for (i=0;i<check_items.length;i++) {
  var x=document.forms["new_form"][check_items[i]].value;
//  alert(x);
  if (x==null || x=="") {

       //alert(check_items[i] +" required!");
       var check_status='<span id="status2"></span>'
       $("#"+check_items[i]).after(check_status)
//       $("#"+check_items[i]).addClass("red")
       var msg_box=$("#status2")
       msg_box.html('<font color="#cc000">required</font>');
       //alert(check_items[i]);
       return false;
    }
  }

});

});

function new_save(type) {

if(type='vhost')
{
  check_items=['hostname', 'eth0', 'eth1', 'hosted', 'gateway', 'project']
} else{ check_items='hostname','eth0','eth1','project' }

  $("#status2").remove();
  for (i=0;i<check_items.length;i++) {
  var x=document.forms["new_form"][check_items[i]].value;
//  alert(x);
  if (x==null || x=="") {

       //alert(check_items[i] +" required!");
       var check_status='<span id="status2"></span>'
       $("#"+check_items[i]).after(check_status)
//       $("#"+check_items[i]).addClass("red")
       var msg_box=$("#status2")
       msg_box.html('<font color="#cc000">required</font>');
       alert(check_items[i]);
       return false;
    }
  }

}
