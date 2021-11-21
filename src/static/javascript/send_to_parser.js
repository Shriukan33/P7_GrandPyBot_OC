// Prevents the form from refreshing the page.
$(function(){
    $("#unparsed_message_form").submit(function(){
        return false
    })
})

// Send message to parser
document.querySelector("#unparsed_message_form").addEventListener("submit", async function() {
    // Get the message
    let message = document.querySelector("#unparsed_message").value
    if (message == "") {
        return false
    }

    var form = new FormData(document.querySelector("#unparsed_message_form"))
    csrftoken = document.getElementsByName("csrf_token")[0].value
    // Send the message to the parser
    messages_html = await fetch("/ajax/parser", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: form
    }).then((myanswer) => {
        document.getElementById("message_history").style.display = "block"
        return myanswer.json()
    });

    $("#message_history").html(messages_html["message_history"])
    lat = messages_html["coordinates"]["lat"]
    lon = messages_html["coordinates"]["lng"]
    initMap(lat, lon)
    // Clear the message
    document.querySelector("#unparsed_message").value = ""

})
