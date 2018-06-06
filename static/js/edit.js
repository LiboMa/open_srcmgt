$(document).ready(function(){

// initialize table
var table_id=$('table').attr('id')
var table = document.getElementById(table_id);
var footer = table.createTFoot();
var row = footer.insertRow(0);
var cell = row.insertCell(0);
var cell1 = row.insertCell(1);
var countrow = table.rows.length;
// column numbers
var colCount = table.rows[0].cells.length
cell.innerHTML="<b>servers:</b>";
cell1.innerHTML=(countrow - 2);

//alert(opt_table)


});

function edit(id){

//alert(requrl+","+callback);
//Set focus on func.
save_cancel();
var ID=id;
//var items = ["hostname","eth0","eth0_vlan","eth1","eth1_vlan","eth2","gateway","os","hosted","project","dmz","datacenter"];
var items=[];

//Dynamic parsing database items by Table Header
var h_keys= document.getElementsByTagName("th")
//alert(h_keys[1].id)
for(i=0;i<h_keys.length;i++) {

  //alert(tagname[i].childNodes[0].nodeValue);
  if (h_keys[i].id != 'th_edit') {
  items.push(h_keys[i].id.replace("th_",""));
  };
};

//alert(items);
//return false;
// #Show to submit items
for(i=0;i<items.length;i++)
  {
  $("#"+items[i]+"_"+ID).hide();
  $("#button_edit_"+ID).hide();
  $("#button_del_"+ID).hide();
  $("#submit_"+items[i]+"_"+ID).val($("#"+items[i]+"_"+ID).text());
  $("#submit_"+items[i]+"_"+ID).show();
  }

$("#btn_save_"+ID).show();
$("#btn_cel_"+ID).show();

$("#btn_cel_"+ID).click(function(){
//$("#ct2").load("./ori_show");
$(".editbox").hide();
$(".text").show();
//$("#edit_"+ID).html()*/
});

};

//Set two button for edit_
// Set this function for post_data
function post_data(id, requrl, callback){
//$("#btn_save_"+id).click(function(){
var data="id="+id;
var url=requrl+'/'+id;

var items=[];

//Dynamic parsing database items by Table Header
var h_keys= document.getElementsByTagName("th")
//alert(h_keys[1].id)
for(i=0;i<h_keys.length;i++) {

  //alert(tagname[i].childNodes[0].nodeValue);
  if (h_keys[i].id != 'th_edit') {
  items.push(h_keys[i].id.replace("th_",""));
   var eid="submit_"+h_keys[i].id +"_"+id;
   // remote spaces from the tail of the string
   var value=$.trim($("#"+eid).val());
   var key="&"+items[i]+"=";
   var info=key+value;
   data+=info;
        };
    };

//alert(data);
//return false;
$.ajax({
       url: url,
       type:'POST',
       data:data,
       async:false,
       dataType:"xml",
       context: document.body,
       success: function(data){
//        $("#ct2").load("./ori_show");
//             sucessFun(data);
         },
       error:function(data){
             errorfun();
           },
       complete:function(obj,str){
         }
}).done(function(){ 

  $("#ct2").load(callback)
  });

};

  
/*var table_type=$('table').attr("id")
    switch(table_type){
      
          case 'vhost_table':
            $("#ct2").load("./ori_show");
            break;
          case 'host_table':
            //        alert('load'+ table_type);
          $("#ct2").load("./hostinfo?no_tpl=yes");
            break;
          default:
          $("#ct2").load("./ori_show");
      
            }
//     table_reload()*/



function new_form(type){

$('#adddiv').show(100);
$.ajax({
    url:"./new?type="+type,
    type:"GET"
  }).done(function(data){ 
        
        $("#adddiv").html(data); 
        });
}

/*function new_entry(type,tableID){

  //parse table..
  //generate row one time
  //handle submit
  //reload page

var items=[];
  
  //Dynamic parsing database items by Table Header
  var h_keys= document.getElementsByTagName("th")
  //alert(h_keys[1].id)
  for(i=0;i<h_keys.length;i++) {
  
    //alert(tagname[i].childNodes[0].nodeValue);
    if (h_keys[i].id != 'th_edit') {
    items.push(h_keys[i].id.replace("th_",""));
    };  
 };

  var table = document.getElementById(tableID);
  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);
  var colCount = table.rows[1].cells.length;

for(var i=0; i<items.length -1; i++){
  var newcell = row.insertCell(i);
  var element=document.createElement("input");
  element.name=items[i]
  element.id=items[i]
  newcell.appendChild(element);
  //alert(newcell.childNodes);
}
 var cell1 = row.insertCell(0);
  var elements1 = document.createElement("input");
  var elements1_1 = document.createElement("span");
  elements1_1.id='hostname_1';
//  elements1_1.class='text';
  elements1_1.text='abc';
  elements1.type="input";
  elements1.name="hostname";
  elements1.id="sub_hostname";
  cell1.appendChild(elements1_1);
  cell1.appendChild(elements1);

}*/

function save_cancel() {

//  $("#editdiv").hide(10);
$(".editbox").hide();
$(".text").show();
  
}

/*function new_save(){

alert("new_save")

var x=document.forms["new_form"]["hostname"].value;
if (x==null || x==""){

    alert("Hostname required!");
    return false;
};

}*/

function new_close(){

$('#adddiv').hide(50);
/*$("#ct2").load('/ori_show');*/
}


function old_delete_entry(id, requrl, callback){

// give the promgt when delete items
var header=document.getElementsByTagName("th")[0].id
var name=$("span#"+header+"_"+id).text();
var r=confirm("Do you want to delete entry of " + name + "?");

var url=requrl + "/" + id

if (r==true) {
$.ajax({
    url: url,
    type: 'POST',
    success:function(){
}
//}).done(function(){window.location.reload(true)});
}).done(function(){

$(".ct2").load(callback)

});
} else {

    return false;
}
}

// this script is used to validate search form. if input body is null then nothing happended.
function validateForm()
{
var x=document.forms["search_form"]["search_body"].value;
if (x==null || x=="")
  {
    //alert("First name must be filled out);
    return false;
    }
}

