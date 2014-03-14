$("#id_course").ready(asyncGetCourseAndBlock);

$("form").submit(function(){
    $("#id_course").prop('disabled', false);
});