gsap.from('.image__svg', {
    duration: 1.5,
    opacity: 0,
    y: '25%'
});

gsap.from('.title__text', {
    duration: 1.5,
    opacity: 0,
    y: '-100%'
});

gsap.from('.title__line', {
    duration: 1.5,
    delay: .5,
    opacity: 0,
    y: '-100%'
});