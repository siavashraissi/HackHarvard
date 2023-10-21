window.addEventListener('scroll', () => {
    const firstDiv = document.getElementById('firstDiv');
    const secondDiv = document.getElementById('secondDiv');
    
    // Get scroll position
    const scrollPosition = window.scrollY + window.innerHeight;

    // Check if the scroll position has passed the first div's bottom
    if (scrollPosition > firstDiv.offsetHeight + 450) { // +150 gives a buffer before transitioning
        firstDiv.classList.add('fade-out');
        secondDiv.classList.add('fade-in');
        firstDiv.classList.remove('fade-in');
        secondDiv.classList.remove('fade-out');
    } else {
        firstDiv.classList.add('fade-in');
        secondDiv.classList.add('fade-out');
        firstDiv.classList.remove('fade-out');
        secondDiv.classList.remove('fade-in');
    }
});
