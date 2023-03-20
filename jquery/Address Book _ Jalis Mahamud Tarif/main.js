$(document).ready(function () {

    $("#form").on("submit", function (e) {
        e.preventDefault();

        let name = $("#name").val();
        let surname = $("#surname").val();
        let phone = $("#phone").val();
        let address = $("#address").val();
        //validate the form fields
        if (name === "") {
            console.log("empty name")
            console.log($(".message")[0])
            $($(".message")[0]).css("display", "block")

        }
        else {
            $($(".message")[0]).css("display", "none")
        }
        if (surname === "") {
            $($(".message")[1]).css("display", "block")


        }
        else {
            $($(".message")[1]).css("display", "none")
        }
        if (phone === "") {
            $($(".message")[2]).css("display", "block")

        }
        else {
            $($(".message")[2]).css("display", "none")
        }
        if (address === "") {
            $($(".message")[3]).css("display", "block")

        }
        else {
            $($(".message")[3]).css("display", "none")
        }
        if (name != "" && surname != "" && phone != "" && address != "") {
            //append data into the table
            let tr = $("<tr>")
            tr.append($("<td>").text(name))
            tr.append($("<td>").text(surname))
            tr.append($("<td>").text(phone))
            tr.append($("<td>").text(address))
            tr.append($("<button id='delete'>").text("X"))
            $("#addressBookData").append(tr)
            $(this)[0].reset();

        }
        else {
            return false
        }

    });

    //delete element
    $(document).on("click", "#delete", function () {
        console.log($(this).parent().html())
        $(this).parent("tr").remove();
    });
    //search element 
    //https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_filters_table
    $("#searchValue").on("keyup", function () {
        var value = $(this).val().toLowerCase();
       
        $("#addressBookData tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
        
    });


});