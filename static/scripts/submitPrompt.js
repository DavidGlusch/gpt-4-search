function submitPrompt($) {
    $('#prompt-submit').on('click', function(e) {
        var prompt = $('#customPrompt').val();
        $.ajax({
            type: "POST",
            url: "/prompt",
            data: { prompt: prompt },
            success: function(response) {
                console.log("The server responded with: " + response);
            }
        });
    });
}
