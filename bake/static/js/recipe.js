function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
});

$('#rec').on('click', function(e){
    e.preventDefault();
    var arrData=[];
    $('#table tr').each(function(){
        var currentRow=$(this);

        var col1_value=currentRow.find("input:eq(0)").val();
        var col2_value=currentRow.find("select").val();
        var col3_value=currentRow.find("input:eq(1)").val();

        var obj={};
        obj.col1=col1_value;
        obj.col2=col2_value;
        obj.col3=col3_value;

        arrData.push(obj);
    })
    var n = 1
    var dict = {}
    for(var x = 0; x < arrData.length; x++){
        if(arrData[x].col1 != ""){
            dict[n] = arrData[x].col1,
            n++
            dict[n] = arrData[x].col2,
            n++
            dict[n] = arrData[x].col3,
            n++
        }
    }
    $.ajax({
        url: 'newrecipe',
        method: 'POST',
        data: {'title': $('#title').val(), 'category': $('#cat').val(), 'directions': $('#dir').val(), 'privacy': $('#pri').val()},
        success: function(){
            $.ajax({
                url: 'ingredients',
                method: 'POST',
                data: dict,
                success: function goToURL(){
                    location.href = 'my_recipes'
                }
            })
        }
    })
})

$('#add_ing').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "adding",
        method: "GET",
        success: function(data){
            $('#table').append(data);
        }
    })
})