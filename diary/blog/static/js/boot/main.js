var image_tag 	= '.sortable-div';	//Блок картинок
var max_image 	= 8; 				//Мах.кол-во картинок
var maxwidth 	= 1024; 			//Ширина картинки
var maxheight 	= 1024;				//Высота картинки

/* Кол-во картинок */
function image_length() {

	$(image_tag + ' div').each(function() {
        $(this).children('input[type=number]').val($(this).index())
    });

	if ($(image_tag + ' div').length < max_image) {
		$('#imgInp').prop('disabled',false);
		$('#imgInp_label').show();
		return true;
	}
	else {
		$('#imgInp').prop('disabled',true);
		$('#imgInp_label').hide();
		return false;
	}
}

/* Удаление блока с картинками*/
function deleteImage(pic) {
	$(pic).parent("div").hide();
	$(pic).siblings('input:hidden[id $= "-DELETE"]').val('on');
	image_length();
	return false;
}

function readURL(input) {
	a = d = $(image_tag + ' div').length*1;

	all = image_length();
    if (all && input.files && input.files[0]) {
        count_files = input.files.length;
        
        for(var i=0; i<count_files; i++) {
	        var reader = new FileReader();
	        d+=1;
	        reader.onload = function (e) {
	        	a++;
	        	var elem = document.getElementById('imgInp');

	        	msg='<div class="formset_row postimages_set dynamic-form">'
	        	+'<div class="newblock"></div>'
	        	+'<input type="hidden" name="postimages_set-'+a+'-post" value="98a9fe3a-7e4d-45fc-a312-a0e2eceda0db" id="id_postimages_set-'+a+'-post">'
	        	+'<input type="hidden" name="postimages_set-'+a+'-id" id="id_postimages_set-'+a+'-id">'
	        	+'<input type="hidden" name="postimages_set-'+a+'-DELETE" id="id_postimages_set-'+a+'-DELETE">'
	        	+'<input type="number" name="postimages_set-'+a+'-order" id="id_postimages_set-'+a+'-order" value="'+a+'">'
	        	+'<img src="'+e.target.result+'" alt="" class="common_tumb_height">'
	        	+'<a class="delete-row" onClick="deleteImage(this);return false;" href="javascript:void(0)">'
	        	+'remove image</a>'
	        	+'</div>';
	            $(image_tag).append(msg);

		        elem.setAttribute('id','postimages_set-'+a+'-image');
	            elem.setAttribute('name','postimages_set-'+a+'-image');

	            $('.newblock').append(elem);	            

            $('.addnewblock').append('<input type="file" style="opddacity: 0; z-index: -1;" id="imgInp" accept="image/*" name="img"/>');	            
	          

	          image_length();
	        }
	        /*
	        var img = new Image;
			img.src = URL.createObjectURL(e.target.result);
			img.onload = function() {
			    var picWidth = this.width;
			    var picHeight = this.height;

			    if (Number(picWidth) > maxwidth || Number(picHeight) > maxheight) {
			        alert("Maximum dimension of the image to be 1024px by 768px");
			        return false;
			    }
			}
			*/
	        reader.readAsDataURL(input.files[i]);
	        if (max_image == d ) {
	        	break;
	       	}
	    }
	  $('#imgInp').val('');
/* $('.addnewblock').append('<input type="file" style="opddacity: 0; z-index: -1;" id="imgInp" accept="image/*" name="img"/>');	            
*/
    }
}

(function($) {
	"use strict"

	$(image_tag).sortable({ 
	    update: function(event, ui) {  
	        image_length();
	    }
	});
 /*alert($(image_tag + ' div').length*1); */  
    $("#imgInp").change(function(){
        readURL(this);
    });

})(jQuery);
