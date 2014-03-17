$("#id_degree").ready(asyncGetCourseAndBlock);

$("form").submit(function(){
    $("#id_degree").prop('disabled', false);
});