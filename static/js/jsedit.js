$(document).ready(function(){

    var table=$('#DT').DataTable({
    
        ordering: true,
        info: true,
// table scroll
        scrollY:"700px",
        //scrollX: true,
        scrollCollapse:true,
        paging: false,
        select: true,

});

$("#DT tbody").on('click','button',function(){

        var btnid=$(this).attr('id');
        var rowid = $(this).parents('tr').attr('id');
        var dict_values = table.row($(this).parents('tr')).data();
        var dict_keys = [];
        var dict = {};

        var counter = 0;

        $('#DT thead th').each(function(){
          // get the table head as the key name of dict
        k = $(this).attr('id');
        dict['id'] = rowid;
        if (k != 'th_edit'){
            
              dict[k] = dict_values[counter];
            
        }
        counter++;
});

        if(btnid==='ebtn') {
        var rowid = $(this).parents('tr').attr('id');
        //alert(rowid);
        //$("#myModal").modal();
        $("input[name=hostname]").attr("readonly",true);
        dialog(rowid, dict);

        } else if (btnid==='dbtn') {
          var r=confirm("Do you want to delete entry of " + dict_values[0] + "?");
          // give the promgt when delete items
          if (r === true){
          delete_entry(rowid, 'delete', './ori_show');
           } else {
            return false;
           };

        }

});

});

function delete_entry(id, requrl, callback){
  
  var url=requrl + "/" + id
  
  $.ajax({
      url: url,
      type: 'POST',
      success:function(){
  }
  //}).done(function(){window.location.reload(true)});
  }).done(function(){
  
  $(".ct2").load(callback)
  });
  
}

function dialog(id, textdata){
    $("#sform").autofill(textdata);

    $('button#bsubmit').click(function() {
                        //remove attr
                        $('#sform input').removeAttr("disabled");
                        //delete tdata;
                        tdata = $('#sform').serialize();
                        //alert(tdata);
      
                        $.ajax({
                          url: "./save/" + id,
                          type: 'POST',
                          data: tdata,
                          context: this,
                          success: function(event){
                              
                              //$(this).dialog('close');
                              //$('#sform').find('input').val('');
                              $(this).remove();
                              
                          },
                            error: function(){
                            alert("failure!"+id);
                          }

                          }).done(function(){
                            $(".ct2").load("./ori_show");
                          }); //$( this ).dialog( "close" );
                          
                    })

        /*$( "#dialog" ).dialog({
//          autoOpen: false, 
            modal: true,
            height: 540,
            width: 500,
            appendTo: "#sform",
            show: {effect: 'fade', duration: 200},

          buttons: [
            {
              text: "ok",
              click: function() {

                  //remove attr
                  $('#sform input').removeAttr("disabled");
                  tdata = $('#sform').serialize();

                  $.ajax({
                    url: "./save/" + id,
                    type: 'POST',
                    data: tdata,
                    context: this,
                    success: function(data){
                        
                        $(this).dialog('close');
                        $(this).remove();
                        
                    }
                    }).done(function(){
                    
                    $(".ct2").load("./ori_show");
                    }); //$( this ).dialog( "close" );
              }
          },

            {
              text: "Cancel",
              context: this,
              click: function() {
                $( this ).dialog( "close" );
              }
            }
          ]
        });*/

}
