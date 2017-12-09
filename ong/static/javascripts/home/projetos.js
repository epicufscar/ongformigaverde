$('.owl-carousel').owlCarousel({
    loop: false,
    margin: 15,
    nav: false,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        },
        1300: {
            items: 5
        }
    }
});