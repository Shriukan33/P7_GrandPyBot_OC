// Prevents the form from refreshing the page.
$(function(){
    $("#unparsed_message_form").submit(function(){
        return false
    })
})

// Send message to parser
document.querySelector("#unparsed_message_form").addEventListener("submit", async function() {
    // Get the message
    console.log("Sending message to parser...")

    let message = document.querySelector("#unparsed_message").value
    if (message == "") {
        return false
    }

    var form = new FormData(document.querySelector("#unparsed_message_form"))
    console.log(form)
    csrftoken = document.getElementsByName("csrf_token")[0].value
    // Send the message to the parser
    messages_html = await fetch("/ajax/parser", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: form
    }).then((messages_html) => {return messages_html.text()})

    $("#message_history").html(messages_html)
    // Clear the message
    document.querySelector("#unparsed_message").value = ""

})
