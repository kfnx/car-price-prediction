document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item');
    const faqToggles = document.querySelectorAll('.faq-toggle');
    
    // Open first FAQ by default
    if (faqItems.length > 0) {
        faqItems[0].classList.add('active');
    }
    
    // Toggle FAQ items
    faqToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const parentItem = this.closest('.faq-item');
            parentItem.classList.toggle('active');
        });
    });
});