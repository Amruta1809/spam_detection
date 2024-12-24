async function checkSpam() {
    const message = document.getElementById('message').value;

    if (!message.trim()) {
        alert("Please enter a message.");
        return;
    }

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = `Prediction: ${data.prediction || data.error}`;
    } catch (error) {
        console.error('Error:', error);
        alert("An error occurred. Check the server console for details.");
    }
}
