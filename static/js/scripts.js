$(document).ready(function () {
    var form =$('#form_buying_excursion');
    form.on('click', function (e) {
        e.preventDefault();
        var submit_btn=$('#submit_btn')
        var excursion_id = submit_btn.data("excursion-id");
        var excursion_name = submit_btn.data("name");
        var excursion_price = submit_btn.data("price");
        console.log(excursion_id);
        console.log(excursion_name);

        var data = {};
        data.excursion_name = excursion_name;
        data.excursion_id = excursion_id;
        var csrf_token = $('#form_buying_excursion [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.excursion_id);
                $('#basket_total_nmb').text()
            }
        })



        $('.basket-items ul').append('<li>'+excursion_name+', '  + ' - ' + excursion_price + 'руб  ' +
            '<a class="delete-item" href="">x</a>'+
            '</li>');

    });

    $('.basket-container').on('click',function (e) {
        e.preventDefault();
        $('.basket-items').removeClass('hidden')
    });

    $('.basket-container').mouseover('click',function (e) {
        e.preventDefault();
        $('.basket-items').removeClass('hidden')
    });

    $('.basket-container').mouseout('click',function (e) {
        e.preventDefault();
        $('.basket-items').addClass('hidden')
    });

    $(document).on('click', '.delete-item', function(e){
         e.preventDefault().
         $(this).closest('li').remove();
     });
});
