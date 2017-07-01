(function( $ ) {

    $('button#encrypt').on('click', function (e) {
        e.preventDefault();
        $.get("/encrypt/",
        {
            original_text: $("#original_text").val(),
            rotation: $('#rotation').val(),
        },
        function(data, status){
            $('#encrypted_text').val(data.encrypted);
        });
    });

    $('button#decrypt').on('click', function (e) {
        e.preventDefault();
        $.get("/decrypt/",
        {
            encrypted_text: $("#encrypted_text").val(),
            rotation: $('#rotation').val(),
        },
        function(data, status){
            $('#original_text').val(data.decrypted);
        });
    });

})( jQuery );