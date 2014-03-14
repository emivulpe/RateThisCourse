$(document).ready(function() {
	syncGetUniAndBlock();
	syncFilterCourses();
});

$("form").submit(function(){
    $("#id_university").prop('disabled', false);
});