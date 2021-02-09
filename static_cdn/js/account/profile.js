//////////////////////////////////////////////////////////////////////////////////
////////////////////////////// tab functionality /////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////

function getParameterByName(name, url = window.location.href) {
  name = name.replace(/[\[\]]/g, '\\$&');
  var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function openTab(evt, tabId) {
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
    if(tabId == 'All') {
        tablinks[0].className = tablinks[0].className += " active"
        for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "block";
        }
    }
    else {
      document.getElementById(tabId).style.display = "block";
      //evt.currentTarget.className += " active";
      evt.target.className += " active";
    }
  }
  
  //document.getElementById("defaultOpen").click();


////////////////////////////////////////////////////////////////////////////////////
////////////////////////////// campain modal functionality ////////////////////////
//////////////////////////////////////////////////////////////////////////////////
/*$('#btnNewCampin').on('click', ()=> {
    $('#newCampain').modal();
});*/


function readProfImage(input, selector) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $(selector).attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

function fillAndOpenProfModel(id=-1, image='', title='', time='', message='', stars=4.5, link='', logo=''){
           console.log(id, image, title, time, message);
           $(`[name=id]`).val(id);
           $(`#id_title`).val(title);
           $(`#id_time`).val(time);
           $(`#id_time`).val(time);
           $(`#id_message`).val(message);
           if(id != -1) {/** edit prof, image not requiered */
            $('#id_image').prop('required',false);
           }else {/** new prof, image requeierd */
            $('#id_image').prop('required',true);
           }
           $(`#displayImage`).attr("src", image);
           $(`#displayImageLogo`).attr("src", logo);
           $('#form_starts').val(stars);
           if(link !='None') {
            $('#id_link').val(link);
           }

           openProfModal();
}

function openProfModal() {
  profModal= profModal.modal();
  $('#id_image').change(function() {
    readProfImage(this, '#displayImage');
  });
  $('#id_logo').change(function() {
    readProfImage(this, '#displayImageLogo');
  })

  
}

function closeProfModal(e) {
  e.preventDefault();
  $.modal.close();
}

var profModal;
$( document ).ready(function() {
  profModal = $('#addProfModel');
  hash = window.location.hash.substring(1);
  var tabBtn = $(`[name=tab_${hash}`);
  tabBtn.click();

  let params = new URLSearchParams(document.location.search.substring(1));
  reviewToEdit=params.get("review");//getParameterByName('review');
  console.log(reviewToEdit);
  if(reviewToEdit != -1 && reviewToEdit != null) {
    history.replaceState(null, "", location.href.split("?")[0] + '#Reviews');
    $(`[name=profEdit${reviewToEdit}]`).click();
  }
});

function deleteCampain(id) {
  $('#deleteModal').attr('data-delurl', '/campain/del/'+id);
  console.log($('#deleteModal').data.delurl);
  $('#deleteModal').modal();
}

function deleteProf(id) {
  $('#deleteModal').attr('data-delurl', '/prof/del/'+id);
  $('#deleteModal').modal();
}