// back to top button function

const _back_to_top = document.querySelector('._back_to_top');

window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    let top = 100; // pixel value from top
    if (document.body.scrollTop > top || document.documentElement.scrollTop > top) {
        _back_to_top.style.bottom = "30px";
    } else {
        _back_to_top.style.bottom = "-30px";
    }

}

_back_to_top.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
})