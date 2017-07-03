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

    $('.break').on('click', function (e) {
        e.preventDefault();
        $.get("/break-cipher/",
        {
            text: $("#encrypted_text").val(),
        },
        function(data, status){
            var resultBox = $('#break_result');
            var keyBox = resultBox.find('.key');
            var textBox = resultBox.find('.text');
            
            keyBox.text(data.key);
            textBox.text(data.decrypted);
            resultBox.removeClass('hidden');
        });
    });

    $('#help_link').on('click', function (e) {
        e.preventDefault();

        $('#modal_backdrop').fadeIn(300);
        $('#modal_help').fadeIn(300);
    });

    $('#modal_backdrop').on('click', function () {
        $('.modal').fadeOut(300);
        $(this).fadeOut(300);
    });
})( jQuery );