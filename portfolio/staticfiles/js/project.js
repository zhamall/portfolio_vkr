document.addEventListener('DOMContentLoaded', function() {
    let slideIndex = 1;
    showSlides(slideIndex);

    function moveSlide(n) {
      slideIndex += n;
      showSlides(slideIndex);
    }

    function showSlides(n) {
        let slides = document.getElementsByClassName('carousel-item');
        if (!slides.length) return;
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex - 1].style.display = "flex";
    }

    // Если moveSlide вызывается из HTML, то нужно сделать функцию глобальной
    window.moveSlide = moveSlide;
});
