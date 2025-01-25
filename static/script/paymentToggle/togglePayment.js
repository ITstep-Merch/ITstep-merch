import { stateCart } from '../index.js';
import {initializePaymentPageElement} from '../paymentInitializeGoods/initializePaymentPageElement.js'

export function togglePayment(ID){   
    const findElementCartButton = document.getElementById(ID)
    const cartsCounter = document.querySelector('.carts-counter');
    localStorage.removeItem(ID)
    stateCart.cartCounterOnPage -= 1;
    cartsCounter.textContent = stateCart.cartCounterOnPage;

    initializePaymentPageElement()
} 
window.togglePayment = togglePayment;  