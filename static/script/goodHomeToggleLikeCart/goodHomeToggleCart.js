import {displayCartedItems} from '../popUpCartLikeDisplayGoods/popUpDisplayCartedItems.js'
import {stateCart} from '../index.js';
import {saveGoodToLocalStorageCart} from '../localStorageSaveItemsCartLike/saveItemsToStorageCart.js'

export function toggleCart(ID){   

    let findElementCartButton = document.getElementById(ID)
    const isHomePage = window.location.pathname === '/';
    const cartsCounter = document.querySelector('.carts-counter');

    if (findElementCartButton == null) {
        localStorage.removeItem(ID)
        displayCartedItems()
        stateCart.cartCounterOnPage -= 1;
        cartsCounter.textContent = stateCart.cartCounterOnPage;
    }

    if(isHomePage){
        const isCarted = findElementCartButton.classList.contains('carted');
        findElementCartButton.classList.toggle('carted')
        if (isCarted) {
            localStorage.removeItem(ID)
            stateCart.cartCounterOnPage -= 1;
            cartsCounter.textContent = stateCart.cartCounterOnPage;
        } else {
            saveGoodToLocalStorageCart(ID);
        }
        displayCartedItems()
        return
    }else{
        findElementCartButton = localStorage.getItem(ID)
        if (findElementCartButton) {
            localStorage.removeItem(ID)
            stateCart.cartCounterOnPage -= 1;
            cartsCounter.textContent = stateCart.cartCounterOnPage;
        }
        displayCartedItems()
        return
    }
}
window.toggleCart = toggleCart;