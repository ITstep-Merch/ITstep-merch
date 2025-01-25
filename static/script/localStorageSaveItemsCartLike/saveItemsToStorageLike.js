import {initializeLikesCounter} from '../popUpCartLikeInitializeCounter/popUpinitializeLikesCouner.js'
import {displayLikedItems} from '../popUpCartLikeDisplayGoods/popUpDisplayLikedItems.js'

export async function saveGoodToLocalStorage(ID) {

    const response = await fetch(`/get_good/${ID}`);
    const goodLikeRes = await response.json();

    let getSize = "Не обрано"

    try {
        const sizeElement = document.getElementById("size");
        if (sizeElement) {
        getSize = sizeElement.value
        }
    } catch (error) {
        console.error("Error getting size element:", error);
    }

    const goodLike = {
        src: goodLikeRes.src,
        name: goodLikeRes.name, 
        code: goodLikeRes.code,
        size: getSize,
        color: goodLikeRes.color,
        price: goodLikeRes.price, 
        id: goodLikeRes.id,
        option: "Like"
    }

    localStorage.setItem(ID, JSON.stringify(goodLike));

    initializeLikesCounter()
    displayLikedItems()
}
window.saveGoodToLocalStorage = saveGoodToLocalStorage;