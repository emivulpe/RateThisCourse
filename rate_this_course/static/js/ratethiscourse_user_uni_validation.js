$("#id_university").ready(function() {
	$('#id_university option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_uni/', function(data) {
    	console.log(data);
    	$('#id_university').val(data).prop('selected', true).prop('disabled', true);
    });
});

$("form").submit(function(){
    $("#id_university").prop('disabled', false);
});