document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById("prediction-form");
    if (!form) return;

    const resultContainer = document.getElementById("result-container");
    const resultEl = document.getElementById("result");
    const errorContainer = document.getElementById("error-container");
    const errorMessageEl = document.getElementById("error-message");
    const loadingIndicator = document.getElementById('loading-indicator');

    // Debounce function
    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Main prediction function
    async function getPrediction() {
        if (!loadingIndicator || !resultEl || !resultContainer || !errorContainer) return;

        loadingIndicator.style.transform = 'scaleX(0.5)';
        resultContainer.classList.remove("hidden");
        errorContainer.classList.add("hidden");
        resultEl.textContent = "Calculating...";

        const formData = new FormData(form);
        const data = {};
        for (const [key, value] of formData.entries()) {
            const element = form.elements[key];
            if (element.type === 'number' || element.type === 'range') {
                data[key] = parseFloat(value);
            } else {
                data[key] = value;
            }
        }

        try {
            const response = await fetch("/predict/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            loadingIndicator.style.transform = 'scaleX(1)';
            setTimeout(() => { loadingIndicator.style.transform = 'scaleX(0)'; }, 300);

            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                const message = errorData?.detail || `HTTP error! status: ${response.status}`;
                throw new Error(message);
            }

            const result = await response.json();
            resultEl.textContent = `$${result.price.toFixed(2)}`;

        } catch (error) {
            loadingIndicator.style.transform = 'scaleX(0)';
            console.error("Error:", error);
            errorMessageEl.textContent = `Failed to get prediction: ${error.message}`;
            errorContainer.classList.remove("hidden");
            resultContainer.classList.add("hidden");
        }
    }

    const debouncedPrediction = debounce(getPrediction, 300);

    // Sync number inputs and sliders
    form.querySelectorAll('input[type="range"]').forEach(slider => {
        const numberInput = document.getElementById(slider.id.replace('-slider', ''));
        if (numberInput) {
            slider.addEventListener('input', (e) => {
                numberInput.value = e.target.value;
            });
            numberInput.addEventListener('input', (e) => {
                slider.value = e.target.value;
            });
        }
    });

    // Add a single event listener to the form for all changes/inputs
    form.addEventListener('input', debouncedPrediction);
    
    // Initial prediction on page load
    getPrediction();
});