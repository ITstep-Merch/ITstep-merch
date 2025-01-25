import {initializeCartsCounter} from '../popUpCartLikeInitializeCounter/popUpInitializeCartsCouner.js'
import {displayCartedItems} from '../popUpCartLikeDisplayGoods/popUpDisplayCartedItems.js'

export async function saveGoodToLocalStorageCart(ID) {
        
        const response = await fetch(`/get_good_cart/${ID}`);
        const goodCartRes = await response.json();
    
        let getSize = "Не обрано"
    
        try {
          const sizeElement = document.getElementById("size");
          if (sizeElement) {
            getSize = sizeElement.value
          }
        } catch (error) {
          console.error("Error getting size element:", error);
        }
        
        const goodCart = {
            src: goodCartRes.src,
            name: goodCartRes.name, 
            code: goodCartRes.code,
            size: getSize,
            color: goodCartRes.color,
            price: goodCartRes.price, 
            id: goodCartRes.id,
            option: "Cart"
        }
    
        localStorage.setItem(ID, JSON.stringify(goodCart));
    
        initializeCartsCounter()
        displayCartedItems()
      }
window.saveGoodToLocalStorageCart = saveGoodToLocalStorageCart;