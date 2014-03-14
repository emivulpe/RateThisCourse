$("#id_course").ready(function() {
	$('#id_course option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_course/', function(data) {
    	console.log(data);
    	$('#id_course').val(data).prop('disabled', true);
    });
});

$("form").submit(function(){
    $("#id_course").prop('disabled', false);
});