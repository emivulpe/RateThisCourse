$("#login_form").submit(function(event){
    event.preventDefault()
    $('#id_inactive_details').prop('hidden', true);
    $('#id_invalid_details').prop('hidden', true);
    signIn();
});