document.getElementById('submit').onclick = function() {
    const email = document.getElementById('email').value.trim();
    const name = document.getElementById('name').value.trim(); // Not required
    const message = document.getElementById('message').value.trim();

    const success = document.getElementById('success');
    const error = document.getElementById('error');

    success.classList.remove('visible');
    error.classList.remove('visible');
    success.textContent = "";
    error.textContent = "";

    if (!email) return showAnswer(error, 'Требуется email');
    if (!message) return showAnswer(error, 'Требуется сообщение');

    showAnswer(success, 'Спасибо! Ваше сообщение отправлено.');
};

function showAnswer(container, text) {
    container.textContent = text;
    container.classList.add('visible');
}
