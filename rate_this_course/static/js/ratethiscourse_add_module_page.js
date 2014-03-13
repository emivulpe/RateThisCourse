$("#id_university").ready(function() {
    $.get('/ratethiscourse/get_user_course/', function(data) {
    	console.log(data);
    	$('#id_university').val(data).prop('disabled', true);
    });
});