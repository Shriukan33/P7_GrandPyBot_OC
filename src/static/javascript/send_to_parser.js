// Prevents the form from refreshing the page.
$(function(){
    $("#unparsed_message_form").submit(function(){
        return false
    })
})

// Send message to parser
document.querySelector("#unparsed_message_form").addEventListener("submit", () => {
    // Get the message
    console.log("Sending message to parser...")
    var form = new FormData(document.querySelector("#unparsed_message_form"))
    console.log(form)
    csrftoken = document.getElementsByName("csrf_token")[0].value
    // Send the message to the parser
    fetch("/ajax/parser", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: form
    })
    // Clear the message
    document.querySelector("#unparsed_message").value = ""

})
