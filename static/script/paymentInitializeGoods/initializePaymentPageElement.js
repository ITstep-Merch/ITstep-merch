import {getItemsFromStorageCart} from '../localStorageGetItemsCartLike/getItemsFromStorageCart.js'
import {togglePayment} from '../paymentToggle/togglePayment.js'

export function initializePaymentPageElement() {
    const cartedItems = getItemsFromStorageCart();
    const cartItemPaymentContainer = document.querySelector('.cart-item-payment-container');

    cartItemPaymentContainer.innerHTML = '';

    cartedItems.forEach(item => {

        const wrapperImgElement = document.createElement('div');
        wrapperImgElement.classList.add('cartedGoodsContainerImageWraper');

        const imgElement = document.createElement('img');
        imgElement.src = item.src; 
        imgElement.alt = 'carted good image'; 
        imgElement.classList.add('cartedGoodsContainerImage');

        wrapperImgElement.appendChild(imgElement);

        const wrapperInfoElement = document.createElement('div');
        wrapperInfoElement.classList.add('cartedGoodsContainerInfoWraper');

        const InfoMainTextElement = document.createElement('a');
        InfoMainTextElement.classList.add('InfoMainTextElement');
        InfoMainTextElement.href = `${baseGoodUrl}${item.id}`;
        InfoMainTextElement.textContent = item.name;
        wrapperInfoElement.appendChild(InfoMainTextElement);

        const wrapperContentElement = document.createElement('div');
        wrapperContentElement.classList.add('cartedGoodsContentElement');
        wrapperContentElement.id = `cart-${item.id}`

        wrapperContentElement.appendChild(wrapperImgElement);
        wrapperContentElement.appendChild(wrapperInfoElement);

        cartItemPaymentContainer.appendChild(wrapperContentElement);

        const InfoMainCodeElement = document.createElement('h2');
        InfoMainCodeElement.classList.add('InfoMainCodeElement');
        InfoMainCodeElement.innerHTML = `<div class="InfoMainElementWraper">
            <span class="InfoMainCodeElementLabel">Артикул:</span> 
            <span class="InfoMainCodeElementValue">${item.code}</span>
        </div>`;
        wrapperInfoElement.appendChild(InfoMainCodeElement);

        const InfoMainSizeElement = document.createElement('h2');
        InfoMainSizeElement.classList.add('InfoMainSizeElement');
        const selectIdPayment = `payment-sizeSelect-${item.id}`;
        InfoMainSizeElement.innerHTML = `<div class="InfoMainElementWraper">
            <span class="InfoMainSizeElementLabel">Розмір:</span> 
            <label for="${selectIdPayment}"></label>
            <select id="${selectIdPayment}" class="InfoMainSizeElementValuePayment">
                <option value="Не обрано">Не обрано</option>
                <option value="XS">XS</option>
                <option value="S">S</option>
                <option value="M">M</option>
                <option value="L">L</option>
                <option value="XL">XL</option>
                <option value="XXL">XXL</option>
            </select>
        </div>`;
        wrapperInfoElement.appendChild(InfoMainSizeElement);
        const sizeSelect = document.getElementById(selectIdPayment);
        console.log(item.size)
        sizeSelect.value = item.size;
        sizeSelect.addEventListener('change', () => {
            const selectedSize = sizeSelect.value;
            item.size = selectedSize; // Оновлюємо об'єкт
            localStorage.setItem(`cart-${item.id}`, JSON.stringify(item)); // Зберігаємо оновлений об'єкт у localStorage
            console.log('Оновлений об\'єкт:', item);
        });

        const InfoColorMainElement = document.createElement('h2');
        InfoColorMainElement.classList.add('InfoColorMainElement');
        InfoColorMainElement.innerHTML = `<div class="InfoMainElementWraper">
            <span class="InfoColorMainElementLabel">Колір:</span> 
            <span class="InfoColorMainElementValue">${item.color}</span>
        </div>`;
        wrapperInfoElement.appendChild(InfoColorMainElement);

        const InfoPriceColorElement = document.createElement('h2');
        InfoPriceColorElement.classList.add('InfoPriceColorElement');
        InfoPriceColorElement.textContent = "₴" + item.price;
        wrapperInfoElement.appendChild(InfoPriceColorElement);

        const InfoElementDeleteButton = document.createElement('button');
        InfoElementDeleteButton.classList.add('InfoElementDeleteButton');
        InfoElementDeleteButton.textContent = "Видалити";
        InfoElementDeleteButton.onclick = function () {
        const converToWithTo = "cart-" + item.id;
        togglePayment(converToWithTo);
        };
        wrapperInfoElement.appendChild(InfoElementDeleteButton);
    });
}
window.initializePaymentPageElement = initializePaymentPageElement;  