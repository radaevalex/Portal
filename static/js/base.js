function displayFooter() {
    let footer = document.getElementsByClassName("footer")[0];
    let prevElem = footer.previousElementSibling;
    let coordPrevElem = prevElem.getBoundingClientRect();
    let footerHight = footer.offsetHeight;
    let heightScreen = document.documentElement.clientHeight;
    if(footerHight + coordPrevElem.bottom < heightScreen){
        footer.style.position = 'fixed';
        footer.style.top = String(heightScreen - footerHight) + 'px';
    }
    else {
        footer.style.position = 'relative';
    }
}
document.addEventListener("DOMContentLoaded", function() {
    displayFooter()
});
document.addEventListener("DOMContentResize", function() {
    displayFooter()
});