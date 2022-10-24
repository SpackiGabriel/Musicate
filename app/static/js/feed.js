gsap.from('.l-module', {
    duration: 1.5,
    opacity: 0,
    y: '-150%'
});

gsap.from('.l-user', {
    duration: 4,
    delay: 1,
    opacity: 0,
    x: '-100%',
    ease: 'elastic'
})

gsap.from('.l-options', {
    duration: 4,
    delay: 1,
    opacity: 0,
    y: '25%',
    ease: 'elastic'
})

function toggleButtons() {
    var options = document.querySelector('.l-options')
    options.classList.toggle('active')
}