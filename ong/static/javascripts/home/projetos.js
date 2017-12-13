$('.owl-carousel').owlCarousel({
    loop: false,
    margin: 15,
    nav: false,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1
        },
        576: {
            items: 1
        },
        768: {
            items: 2
        },
        1300: {
            items: 3
        },
        2000: {
            items: 4
        },
        2500: {
            items: 5
        }
    }
});