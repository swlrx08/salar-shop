// import data from "./src/dom/data";

console.log("working fine");

const monthNames = ["Jan", "Feb", "Mar", "April", "May", "June",
    "July", "Aug", "Sept", "Oct", "Nov", "Dec"
];

$("#commentForm").submit(function (e) {
    e.preventDefault();

    let dt = new Date();
    let time = dt.getDate() + "" + monthNames[dt.getUTCMonth()] + ", " + dt.getFullYear()

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

                let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                _html += '<div class="user justify-content-between d-flex">'
                _html += '<div class="thumb text-center">'
                _html += '<img src="' + images + '" alt=""/>'
                _html += '<a href="#" class="font-heading text-brand">' + res.context.user + '</a>'
                _html += '</div>'

                _html += '<div class="desc">'
                _html += '<div class="d-flex justify-content-between mb-10">'
                _html += '<div class="d-flex align-items-center">'
                _html += '<span class="font-xs text-muted">' + time + ' </span>'
                _html += '</div>'

                for (let i = 1; i <= res.context.rating; i++) {
                    _html += '<i class="fas fa-star text-warning"></i>'
                }

                _html += '</div>'
                _html += '<p class="mb-10">' + res.context.review + '</p>'

                _html += '</div>'
                _html += '</div>'
                _html += '</div>'

                $(".comment-list").prepend(_html)

            }
        }
    })
})


$(document).ready(function () {
    $(".filter-checkbox , #price-filter-btn").on("click", function () {
        console.log("A checkbox have been clicked");

        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;


        $(".filter-checkbox").each(function () {
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")  // vendor or category

            // console.log("Filter value is:", filter_value);
            // console.log("Filter value is:", filter_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function (element) {
                return element.value
            })
        })
        console.log("Filter object is:", filter_object);
        $.ajax({
            url: '/filter-products/',
            data: filter_object,
            dataType: 'json',
            beforeSend: function () {
                console.log("Trying to  filter product...");
            },
            success: function (response) {
                console.log(response);
                console.log("Data filtered successfully");
                $('#filter-product').html(response.data)
            }
        })
    })
    $("#max_price").on("blur", function () {
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        // console.log("Current Price Is:", current_price);
        // console.log("Max Price Is:", max_price);
        // console.log("Min Price Is:", min_price);


        if (current_price < parseInt(min_price) || current_price > parseInt(max_price)) {
            // console.log("Price Error");

            min_price = Math.round(min_price * 100) / 100
            max_price = Math.round(max_price * 100) / 100

            alert("Price must between $" + min_price + " and $" + max_price)
            $(this).val(min_price)
            $('#range').val(min_price)

            $(this).focus()

            return false

        }
    })

})


// Add to card func
//new
$(".add-to-cart-btn").on("click", function () {

    let this_val = $(this)
    let index = this_val.attr("data-index")


    let quantity = $(".product-quantity-" + index).val()
    let product_title = $(".product-title-"+ index).val()

    let product_id = $(".product-id-"+ index).val()
    let product_price = $(".current-product-price-" + index ).text()

    let product_pid = $(".product-pid-" + index ).val()
    let product_img = $(".product-img-" + index ).val()


    console.log("Quantity", quantity);
    console.log("Title", product_title);
    console.log("Price", product_price);
    console.log("ID", product_id);
    console.log("PID", product_pid);
    console.log("Image", product_img);
    console.log("Index", index);
    console.log("Current Element", this_val);


    $.ajax({
        url: "/add-to-cart",
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_img,
            'qty': quantity,
            'title': product_title,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function () {
            console.log("Adding product to Cart...");
        },
        success: function (response) {
            this_val.html("✔")
            console.log("Added product to Cart!");
            $(".cart-items-count").text(response.total_cart_items)

        },
    })
})


//old
// $("#add-to-card-btn").on("click", function (){
//     let quantity = $("#product-quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let product_price = $("#current-product-price").text()
//     let this_val = $(this)
//
//
//     console.log("Quantity", quantity);
//     console.log("Title", product_title);
//     console.log("Price", product_price);
//     console.log("ID", product_id);
//     console.log("Current Element", this_val);
//
//
//     $.ajax({
//         url : "/add-to-cart",
//         data : {
//             'id' : product_id,
//             'qty' : quantity,
//             'title': product_title,
//             'price' : product_price,
//         },
//         dataType:'json',
//         beforeSend: function (){
//             console.log("Adding product to Cart...");
//         },
//         success: function (response){
//             this_val.html("Item added to cart")
//             console.log("Added product to Cart!");
//             $(".cart-items-count").text(response.total_cart_items)
//
//         },
//     })
// })


