import { stateCart } from '../index.js';

export function initializeCartsCounter() {
    const cartsCounter = document.querySelector('.carts-counter');
    stateCart.cartCounterOnPage = 0;

    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key.startsWith('cart-')) {
        const item = JSON.parse(localStorage.getItem(key) || "{}");

        if (item.option === "Cart") {
            stateCart.cartCounterOnPage += 1;
        }
        }

        const idForGood = document.getElementById(key);
    }

    if (cartsCounter) {
        cartsCounter.textContent = stateCart.cartCounterOnPage;
    }
}
window.initializeCartsCounter = initializeCartsCounter;












