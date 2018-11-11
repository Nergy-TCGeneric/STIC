var opacity = 1;

function DoFadeOut() {
    if(opacity > 0) {
        opacity -= .1;
        setTimeout(function(){DoFadeOut()}, 100);
    } 
    document.getElementsByTagName("section")[0].style.opacity = opacity;
}

document.onscroll = DoFadeOut;