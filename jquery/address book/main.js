$(document).ready(function () {
    function resetForm() {
        $("form")[0].reset();
    }

    $("#form").on("submit", function (e) {
        e.preventDefault();
        let name = $("#name").val();
        let surname = $("#surname").val();
        let phone = $("#phone").val();
        let address = $("#address").val();
        //add data
        let tr = $("<tr>")
        tr.append($("<td>").text(name))
        tr.append($("<td>").text(surname))
        tr.append($("<td>").text(phone))
        tr.append($("<td>").text(address))
        tr.append($("<button id='delete'>").text("X"))
        $("#data").append(tr)
        $(this)[0].reset();
        // resetForm();




    });
    //delete
    $(document).on("click", "#delete", function () {
        console.log($(this).parent().html())
        $(this).parent("tr").remove();
    });
    //search
    $("#searchValue").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        // console.log(value)
        $("#addressData tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
        // console.log($("#addressData tr").html())
    });


});