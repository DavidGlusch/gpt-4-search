function togglePrompt($) {
    $('#prompt-switch').change(function() {
        if(this.checked) {
            $('#customPrompt').prop('disabled', false);
        } else {
            $('#customPrompt').prop('disabled', true);
        }
    });
}
