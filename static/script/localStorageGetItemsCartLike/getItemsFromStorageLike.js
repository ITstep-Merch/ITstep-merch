export function getItemsFromStorage(){
    let listElementsFromStorage = []

    for (let i = 0; i < localStorage.length; i++){
        let itemFromStorageKey = localStorage.key(i)
        let itemFromStorageValye = localStorage.getItem(itemFromStorageKey)
        let itemFromStorageValyeParce = JSON.parse(itemFromStorageValye)
        if (itemFromStorageValyeParce.option === "Like"){
        listElementsFromStorage.push(itemFromStorageValyeParce)
        }
    }
    return listElementsFromStorage
}
window.getItemsFromStorage = getItemsFromStorage;