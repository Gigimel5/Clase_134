//Crear la variable date - (fecha).
var date = new Date()
var dateS = "Fecha: " + date.toLocaleDateString()

//Cargar HTML DOM.
$(document).ready(function () {
    $("#display_date").html(dateS)
})

//Definir la variable para almacenar la emoción predecida.
var emotion2

//HTML-->JavaScript--->Flask.
//Flask--->JavaScript--->HTML.

//Selector jQuery y la acción click.

$(function () {
    $("#predict_button").click(function () {
        var inputText = {
            "text": $("#text").val()
        }
        //Llamada a AJAX 
        $.ajax({
            type: "POST",
            url: "/predict-emotion",
            data: JSON.stringify(inputText),
            dataType: "json",
            contentType: "application/json",
            success: function (result) {
                emotion2 = result.data.emotion
                emoticon2 = result.data.emoticon
                $("#prediction").html(emocion)
                $("#prediction").css("display", "block")
                $("#emo_img_url").attr("src", emoticon2)
                $("#emo_img_url").css("display", "block")
            },
            error: function (result) {
                alert(result.responseJSON.message)
            }

            // Resultado recibido de Flask ----->JavaScript

            // Mostrar resultado usando JavaScript----->HTML

            //Función error 

        });
    });
})

