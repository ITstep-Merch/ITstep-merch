export function totalPriceValye(){
  // document.addEventListener('DOMContentLoaded', function() {
    const list = getItemsFromStorageCart()

    let totalPrice = 0;
    
    list.forEach(item => {
      totalPrice += item.price
    })
    document.querySelector('.total-price-valye').innerHTML = totalPrice;
  // })
}
window.totalPriceValye = totalPriceValye; 