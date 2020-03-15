$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    })
});

function open_stic_wiki(name) {
    $.ajax({
        type: "GET",
        url: "http://stic.dothome.co.kr/w/api.php",
        data: {
            action: "parse",
            page: name,
            prop: "text",
            formatversion: "2",
            format: "json"
        },
        dataType: "json"
    })
    .done(function(json) {
        var title = ""
        if(json['parse']['title']) title = "<h1>" + json['parse']['title'] + "</h1>";
        else title = "<h1>" + "제목 없음" + "</h1>";
        document.getElementById("wiki_viewer").innerHTML = title + json['parse']['text'];
    })
    .fail(function(xhr, status, errorThrown) {
        console.log(status, errorThrown);
        const title = "<h1>" + "이런!" + "</h1>";
        document.getElementById("wiki_viewer").innerHTML = title + "데이터를 받아오는데 실패했습니다. 잠시 후 다시 시도해주세요.";
    })
    .always(function() {
        $("#wiki_viewer").addClass('active');
    });
}

function close_stic_wiki() {
    document.getElementById("wiki_viewer").innerHTML = "";
    $("#wiki_viewer").removeClass('active');
}