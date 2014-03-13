$("#id_university").change(function() {
    var uni_id = $('#id_university').find(":selected").attr("value");
    var $course = $("#id_course");
    $.get('/ratethiscourse/get_courses/',{university_id: uni_id}, function(data) {
    	console.log(data);
        $course.empty();
        $.each(data, function(index, value) {
            $course.append($("<option></option>").attr("value", data[index][0]).text(data[index][1]));
        });
    });
});