$(document).ready(function () {
    function resetForm() {
        $("form")[0].reset();
    }
    $("#form").on("submit", function (e) {
        e.preventDefault();
        let name = $("#name").val();
        let surname = $("#surname").val();
        let mobile = $("#mobile").val();
        let address = $("#address").val();
        //add data
        let tr = $("<tr>")
        tr.append($("<th>").text(name))
        tr.append($("<th>").text(surname))
        tr.append($("<th>").text(mobile))
        tr.append($("<th>").text(address))
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

});