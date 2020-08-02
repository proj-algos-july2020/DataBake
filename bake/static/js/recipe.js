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

$('#doughs').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "doughs",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#doughs').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#creams').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "creams",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#creams').removeClass('nav-link').addClass('nav-link active')
            $('#doughs').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#mousses').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mousses",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mousses').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#doughs').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#glazes').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "glazes",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#glazes').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#doughs').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#sponges').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "sponges",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#sponges').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#doughs').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#syrups').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "syrups",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#syrups').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#doughs').removeClass('active')
            $('#confection').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#confection').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "confection",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#confection').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#doughs').removeClass('active')
            $('#other').removeClass('active')
        }
    });
});
$('#other').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "other",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#other').removeClass('nav-link').addClass('nav-link active')
            $('#creams').removeClass('active')
            $('#mousses').removeClass('active')
            $('#glazes').removeClass('active')
            $('#sponges').removeClass('active')
            $('#syrups').removeClass('active')
            $('#confection').removeClass('active')
            $('#doughs').removeClass('active')
        }
    });
});

$('#mdoughs').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mdoughs",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mdoughs').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#mcreams').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mcreams",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mcreams').removeClass('nav-link').addClass('nav-link active')
            $('#mdoughs').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#mmousses').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mmousses",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mmousses').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mdoughs').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#mglazes').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mglazes",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mglazes').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mdoughs').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#msponges').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "msponges",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#msponges').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#mdoughs').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#msyrups').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "msyrups",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#msyrups').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#mdoughs').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#mconfection').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mconfection",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mconfection').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mdoughs').removeClass('active')
            $('#mother').removeClass('active')
        }
    });
});
$('#mother').click(function(e){
    e.preventDefault();
    $.ajax({
        url: "mother",
        method: "POST",
        success: function(data){
            $('#pageload').html(data);
            $('#mother').removeClass('nav-link').addClass('nav-link active')
            $('#mcreams').removeClass('active')
            $('#mmousses').removeClass('active')
            $('#mglazes').removeClass('active')
            $('#msponges').removeClass('active')
            $('#msyrups').removeClass('active')
            $('#mconfection').removeClass('active')
            $('#mdoughs').removeClass('active')
        }
    });
});