function selectAndDisableElement(elementID, data) {
    if (data != "") {
        $(elementID).val(data).prop('selected', true).prop('disabled', true);
    }
}

function asyncGetUniAndBlock() {
	$('#id_university option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_uni/', function(data) {
    	console.log(data);
        selectAndDisableElement('#id_university', data);
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
            selectAndDisableElement('#id_university', data);
        } 
    });
};

function asyncGetCourseAndBlock() {
    $('#id_degree option:selected').prop('selected', false);
    $.get('/ratethiscourse/get_user_course/', function(data) {
        console.log(data);
        selectAndDisableElement('#id_degree', data);
    });
};

function syncGetCourseAndBlock() {
    $('#id_degree option:selected').prop('selected', false);
    $.ajax({
        url: '/ratethiscourse/get_user_course/',
        type: 'GET',
        async: false,
        success: function(data) {
            console.log(data);
            selectAndDisableElement('#id_degree', data);
        } 
    });
};

function asyncFilterCourses() {
    var uni_id = $('#id_university').find(":selected").attr("value");
    var $degree = $("#id_degree");
    $degree.prop('disabled', true);
    $.get('/ratethiscourse/get_courses/', {university_id: uni_id}, function(data) {
    	console.log("second");
    	console.log(data);
        $degree.empty();
        $.each(data, function(index, value) {
            $degree.append($("<option></option>").attr("value", data[index][0]).text(data[index][1]));
        });
        $degree.prop('disabled', false);
    });
};

function syncFilterCourses() {
    var uni_id = $('#id_university').find(":selected").attr("value");
    var $degree = $("#id_degree");
    $degree.prop('disabled', true);
    var result = null;
    $.ajax({
    	url: '/ratethiscourse/get_courses/',
        data: {university_id: uni_id},
        type: 'GET',
        async: false,
        success: function(data) {
        	console.log(data);
    		$degree.empty();
        	$.each(data, function(index, value) {
           		$degree.append($("<option></option>").attr("value", data[index][0]).text(data[index][1]));
        	});
            $degree.prop('disabled', false);
        } 
    });
    
};

function emptyList() {
    var $course = $('#id_course');
    $course.empty();
    $course.append($("<option></option>").attr("value", "").text("---------"));
}

function signIn() {
    $("input:submit").prop('disabled', true);
    $.ajax({
        url: '/ratethiscourse/ajax_login/',
        type: 'POST',
        data: $('#login_form').serialize(),
        success: function(data) {
            console.log(data);
            if (data == 'valid') {
                $("#loginModalid").modal({"backdrop": "static"});
                location.reload();
            } else if (data == 'invalid') {
                $('#id_invalid_details').prop('hidden', false);
            } else if (data == 'inactive') {
                $('#id_inactive_details').prop('hidden', false);
            }
            $("input:submit").prop('disabled', false);
        }
    });
}

function signOut() {
    $.ajax({
        url: '/ratethiscourse/ajax_logout/',
        type: 'GET',
        success: function(data) {
            window.location.href = "http://gucsteamh.pythonanywhere.com/ratethiscourse/";
            // location.reload();
        }
    })
}