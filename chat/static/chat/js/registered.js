const messages = document.querySelectorAll('.message');

setTimeout(function() {
    messages.forEach((message) => {
        message.classList.add('fade-in');

        message.addEventListener('animationend', function() {
            message.classList.remove('fade-in');
        }, { once: true });

        message.addEventListener('click', function() {
            message.classList.toggle('selected');
        });

        message.addEventListener('dblclick', function() {
            message.remove();
        });

        setTimeout(() => {
            message.classList.add('fade-out');

            message.addEventListener('animationend', () => {
                message.remove();
            }, { once: true });

        }, 2000);

    });
}, 1000);


document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.connect-form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // Stop form from submitting
            const button = form.querySelector('.connect_button');
            button.textContent = 'Disconnected';
            button.disabled = true;
            button.classList.add('disconnected');
        });
    });
});

console.log("registered.js loaded!");

