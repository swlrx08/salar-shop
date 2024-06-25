console.log("working fine");

$("#commentForm").submit(function(e) {
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function (response){
            console.log("Comment Saved to DB...")
        }
    })
})