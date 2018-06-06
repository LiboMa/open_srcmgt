$(document).ready(function(){

});


function destroy_status() {
                            
 $("#readinput").parent().removeClass("has-error");
 $("#readinput").parent().removeClass("has-success");
 $("#success_info").remove();
 $("#error_info").remove();

}

function add_dialog(url, callbak){

        // initialized table;
        destroy_status();
        $("#sform input").val("");
        //$("#sform select").val("");
        $("input[name=hostname]").removeAttr("readonly");
        // validation of hostname
        var msg_success='<span id="success_info" class="glyphicon glyphicon-ok form-control-feedback"></span>';
        var msg_error='<span id="error_info" class="glyphicon glyphicon-remove form-control-feedback"></span>';
        $("#readinput").change(function(){

            destroy_status();
            var hostname = $(this).val();
              if(hostname.length > 3){
             
                $.ajax({
                  type:"POST",
                  url:"check_host",
                  data:"hostname=" + hostname,
                  success:function(msg){
                        if ( msg === 'OK') {
                            //alert(msg_success);
                            //destroy_status();
                            var info=msg_success
                            var css='has-success'
                        } else {

                            var info=msg_error
                            var css='has-error'
                            //destroy_status();
                        }
                        $("#readinput").parent().addClass(css);
                        $('#readinput').after(info);
                  }

                 }).done(function(){
                   //destroy_status();
                 });
              } else if(hostname.length == 0){

                $("#success_info").remove();
                $("#error_info").remove();

              }

             // }

        });
            /*var msgbox = $("#status");
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

        
        })*/

        // serialize data 
        $("button#bsubmit").click(function() {

                // remove attr
                //$("input[name=id]").remove()
                $('#sform input').removeAttr("disabled");
                $('#sform input[name=id]').remove();
                tdata = $('#sform').serialize();

                $.ajax({
                  url: "./new?type=vhost",
                  type: 'POST',
                  data: tdata,
                  context: this,
                  success: function(data){
                      console.log(tdata);
                  //    $(this).dialog('close');
                      $(this).remove();
                  },
                  error: function(){
                        alert("failure");
                        console.log(tdata);
                  
                        }

                  }).done(function(){
                  
                    $(".ct2").load("./ori_show");
                  }); //$( this ).dialog( "close" );
            });

}
