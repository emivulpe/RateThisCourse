function asyncGetUniAndBlock() {
	$('#id_university option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_uni/', function(data) {
    	console.log("first");
    	console.log(data);
    	if (data != "") {
    		$('#id_university').val(data).prop('selected', true).prop('disabled', true);
    	}
    });
};

function syncGetUniAndBlock() {
    $('#id_university option:selected').prop('selected', false);
    $.ajax({
        url: '/ratethiscourse/get_user_uni/',
        type: 'GET',
        async: false,
        success: function(data) {
            console.log(data);
            if (data != "") {
                $('#id_university').val(data).prop('selected', true).prop('disabled', true);
            }
        } 
    });
};

function asyncGetCourseAndBlock() {
    $('#id_course option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_course/', function(data) {
        console.log(data);
        if (data != "") {
            $('#id_course').val(data).prop('disabled', true);
        }
    });
};

function syncGetCourseAndBlock() {
    $('#id_course option:selected').prop('selected', false);
    $.ajax({
        url: '/ratethiscourse/get_user_course/',
        type: 'GET',
        async: false,
        success: function(data) {
            console.log(data);
            if (data != "") {
                $('#id_course').val(data).prop('disabled', true);
            }
        } 
    });
};

function asyncFilterCourses() {
    var uni_id = $('#id_university').find(":selected").attr("value");
    var $course = $("#id_course");
    $course.prop('disabled', true);
    $.get('/ratethiscourse/get_courses/', {university_id: uni_id}, function(data) {
    	console.log("second");
    	console.log(data);
        $course.empty();
        $.each(data, function(index, value) {
            $course.append($("<option></option>").attr("value", data[index][0]).text(data[index][1]));
        });
    });
    $course.prop('disabled', false);
};

function syncFilterCourses() {
    var uni_id = $('#id_university').find(":selected").attr("value");
    var $course = $("#id_course");
    $course.prop('disabled', true);
    var result = null;
    $.ajax({
    	url: '/ratethiscourse/get_courses/',
        data: {university_id: uni_id},
        type: 'GET',
        async: false,
        success: function(data) {
        	console.log(data);
    		$course.empty();
        	$.each(data, function(index, value) {
           		$course.append($("<option></option>").attr("value", data[index][0]).text(data[index][1]));
        	});
        } 
    });
    $course.prop('disabled', false);
};

function emptyList() {
    var $course = $('#id_course');
    $course.empty();
    $course.append($("<option></option>").attr("value", "").text("---------"));
}