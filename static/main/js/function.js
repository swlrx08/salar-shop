console.log("working fine");

const monthNames = ["Jan","Feb","Mar","April","May","June",
    "July","Aug","Sept","Oct","Nov", "Dec"
];

$("#commentForm").submit(function (e) {
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDate() + "" + monthNames[dt.getUTCMonth()]+ ", "+ dt.getFullYear()

    let images = $('#myImg').attr('src')

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function (res) {
            console.log("Comment Saved to DB...")


            if (res.bool == true) {
                $("#review-res").html("Review Added Successfully")
                $(".hide-comment-form").hide()
                $(".add-review").hide()

                let _html ='<div class="single-comment justify-content-between d-flex mb-30">'
                        _html +=  '<div class="user justify-content-between d-flex">'
                        _html += '<div class="thumb text-center">'
                        _html += '<img src="'+ images +'" alt=""/>'
                        _html += '<a href="#" class="font-heading text-brand">'+ res.context.user +'</a>'
                        _html += '</div>'

                        _html += '<div class="desc">'
                        _html += '<div class="d-flex justify-content-between mb-10">'
                        _html += '<div class="d-flex align-items-center">'
                        _html += '<span class="font-xs text-muted">'+ time +' </span>'
                        _html += '</div>'

                        for (let i =1; i<= res.context.rating; i++){
                            _html += '<i class="fas fa-star text-warning"></i>'
                        }

                        _html += '</div>'
                        _html += '<p class="mb-10">'+ res.context.review +'</p>'

                        _html += '</div>'
                        _html += '</div>'
                        _html += '</div>'

                        $(".comment-list").prepend(_html)

                }
        }
    })
})