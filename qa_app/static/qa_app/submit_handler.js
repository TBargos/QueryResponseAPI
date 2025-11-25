document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', submitForm);
});

function submitForm (event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    let obj = {};
    formData.forEach((value, key) => obj[key] = value);

    let request = new Request(event.target.action, {
        method: 'POST',
        body: JSON.stringify(obj),
        headers: {
            'Content-Type': 'application/json',
        },
    });

    fetch(request).then(response => {
        if (!response.ok) {
            throw new Error('Ошибка сети: ' + response.status)
        }
        return response.json()
    }).then(data => {
        console.log('Ответ от сервера:', data)
    }).catch(error => {
        console.error('Ошибка запроса:', error)
    });
}