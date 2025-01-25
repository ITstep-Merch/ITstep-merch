import {displayLikedItems} from '../popUpCartLikeDisplayGoods/popUpDisplayLikedItems.js'
import {stateLike} from '../index.js';
import {saveGoodToLocalStorage} from '../localStorageSaveItemsCartLike/saveItemsToStorageLike.js'

export function toggleLike(ID){

    const likesCounter = document.querySelector('.likes-counter');
    let findElementLikeButton = document.getElementById(ID)
    const isHomePage = window.location.pathname === '/';

    if (findElementLikeButton == null) {
        localStorage.removeItem(ID)
        displayLikedItems()
        stateLike.likeCounter -= 1;
        likesCounter.textContent = stateLike.likeCounter;
    }

    if (localStorage.getItem(ID) || isHomePage) {
        const isLiked = findElementLikeButton.classList.contains('liked');
        findElementLikeButton.classList.toggle('liked')
        if (isLiked) {
            localStorage.removeItem(ID)
            stateLike.likeCounter -= 1;
            likesCounter.textContent = stateLike.likeCounter;
        } else {
            saveGoodToLocalStorage(ID);
        }
        displayLikedItems()
        return
    } else {
        findElementLikeButton = localStorage.getItem(ID)
        if (findElementLikeButton) {
            localStorage.removeItem(ID)
            stateLike.likeCounter -= 1;
            likesCounter.textContent = stateLike.likeCounter;
        } 
        displayLikedItems()
        return
    }
}
window.toggleLike = toggleLike;