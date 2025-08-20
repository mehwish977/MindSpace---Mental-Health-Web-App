// Example: Random floating positions
const ellipses = document.querySelectorAll('.ellipse');

ellipses.forEach((el, idx) => {
    let delay = Math.random() * 5;
    el.style.animationDelay = `${delay}s`;
});

// Optional: random glow effect on cards
const menuCards = document.querySelectorAll('.menu-card');

menuCards.forEach(card => {
    card.addEventListener('mouseover', () => {
        card.style.boxShadow = '0 0 20px rgba(255,255,255,0.5)';
    });
    card.addEventListener('mouseout', () => {
        card.style.boxShadow = 'none';
    });
});
