import { stateLike } from '../index.js';

export function initializeLikesCounter() {
    const likesCounter = document.querySelector('.likes-counter');
    stateLike.likeCounter = 0;

    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        const item = JSON.parse(localStorage.getItem(key) || "{}");

        if (item.option === "Like") {
            stateLike.likeCounter += 1;
        }

        const idForGood = document.getElementById(key);
    }

    if (likesCounter) {
        likesCounter.textContent = stateLike.likeCounter;
    }
}
window.initializeLikesCounter = initializeLikesCounter;












