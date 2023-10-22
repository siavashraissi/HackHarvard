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

document.addEventListener("DOMContentLoaded", function() {
    const submitButton = document.getElementById("submit-button");
    const linkInput = document.getElementById("link");

    submitButton.addEventListener("click", function(e) {
        e.preventDefault();  // Prevent the default form submission behavior

        fetch('/submit', {
            method: 'POST',
            body: new URLSearchParams('link=' + linkInput.value),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log("message received")
            // Display the message received from the Flask server
            const messageDiv = document.createElement("div");
            messageDiv.innerText = data.message;
            document.body.appendChild(messageDiv);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

