

let predicted_emotion;

$(function () {
    $("#predict_button").click(() => {
        let input_data = {
            "text": $("#text").val()
        }
        console.log(input_data)
        $.ajax({
            type: 'POST',
            url: "/predict-emotion",
            data: JSON.stringify(input_data),
            dataType: "json",
            contentType: 'application/json',
            success: (result) => {
                predicted_emotion = result.data.predicted_emotion;
                emo_url = result.data.predicted_emotion_img_url;
                $("#result").css("display", "flex");
                $("#prediction").html(predicted_emotion);
                $("#emo_img_url").attr('src', emo_url);
            },
            error: (result) => {
                alert(result.responseJSON.message)
            }
        });
    });
})
