$("form").submit(function(){
	console.log("submit");
    $("input:submit").prop('disabled', true);
});