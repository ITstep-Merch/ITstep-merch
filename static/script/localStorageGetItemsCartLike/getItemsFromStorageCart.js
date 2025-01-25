export function getItemsFromStorageCart(){
    let listElementsFromStorageCart = []

    for (let i = 0; i < localStorage.length; i++){
        let itemFromStorageKey = localStorage.key(i)
        if (itemFromStorageKey.startsWith('cart-')) {
        let itemFromStorageValye = localStorage.getItem(itemFromStorageKey)
        let itemFromStorageValyeParce = JSON.parse(itemFromStorageValye)
        if (itemFromStorageValyeParce.option === "Cart"){
            listElementsFromStorageCart.push(itemFromStorageValyeParce)
        }
        }
    }
    return listElementsFromStorageCart
}
window.getItemsFromStorageCart = getItemsFromStorageCart;