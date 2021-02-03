//////////////////////////////////////////////////////////////////////////////////
////////////////////////////// tab functionality /////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////
function openTab(evt, tabId) {
  debugger;
    window.location.hash = tabId;
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabId).style.display = "block";
    //evt.currentTarget.className += " active";
    evt.target.className += " active";
  }
  
  //document.getElementById("defaultOpen").click();


////////////////////////////////////////////////////////////////////////////////////
////////////////////////////// campain modal functionality ////////////////////////
//////////////////////////////////////////////////////////////////////////////////
$('#btnNewCampin').on('click', ()=> {
    $('#newCampain').modal();
});
function readProfImage(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#displayImage').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

function fillAndOpenProfModel(id=-1, image='', title='', time='', message=''){
           console.log(id, image, title, time, message);
           debugger;
           $(`[name=id]`).val(id);
           $(`#id_title`).val(title);
           $(`#id_time`).val(time);
           $(`#id_time`).val(time);
           $(`#id_message`).val(message);
           if(id != -1) {
            $('#id_image').prop('required',false);
           }else {
            $('#id_image').prop('required',true);
           }
           $(`#displayImage`).attr("src", image);
           openProfModal();
}

function openProfModal() {
  profModal= profModal.modal();
  $('#id_image').change(function() {
    readProfImage(this);
  })
  
}

function closeProfModal(e) {
  e.preventDefault();
  $.modal.close();
}

var profModal;
$( document ).ready(function() {
  debugger;
  profModal = $('#addProfModel');
  hash = window.location.hash.substring(1);
  var tabBtn = $(`[name=tab_${hash}`);
  tabBtn.click();
});