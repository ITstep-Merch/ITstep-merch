import {initializeCartsCounter} from '../popUpCartLikeInitializeCounter/popUpInitializeCartsCouner.js'

export function animateCart(ID){
    initializeCartsCounter()
    const cartButton = document.querySelector('.cart-good-catalog');
    const cartButtonID = document.getElementById(ID);
        
    cartButtonID.classList.add('animate');
    setTimeout(() => {
        cartButtonID.classList.remove('animate');
    }, 450); 
}  
window.animateCart = animateCart;