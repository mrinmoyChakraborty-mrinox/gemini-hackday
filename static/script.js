const form = document.getElementById('emailForm');
const responseDiv = document.getElementById('responseContainer');

form.onsubmit = function(e) {
    e.preventDefault();
    
    const purpose = document.getElementById('purpose').value;
    const tone = document.querySelector('input[name="tone"]:checked').value;
    
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `purpose=${encodeURIComponent(purpose)}&tone=${encodeURIComponent(tone)}`
    })
    .then(response => response.text())
    .then(result => {
        responseDiv.innerHTML = result.replace(/\n/g, '<br>');
        responseDiv.style.display = 'block';
    });
};
