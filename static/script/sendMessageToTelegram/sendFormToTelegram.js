import {getItemsFromStorageCart} from '../localStorageGetItemsCartLike/getItemsFromStorageCart.js'

const nameInput = document.getElementById('name-input');
const secondNameInput = document.getElementById('second-name-input');
const fatherNameInput = document.getElementById('father-name-input');
const emailInput = document.getElementById('email-input');
const phoneInput = document.getElementById('phone-input');
const confirmOrderBtn = document.querySelector('.confirm-order-btn');
const methodCheckboxText = document.getElementById('method-checkbox-text');
const methodCheckbox = document.getElementById('method-checkbox');
const oblastInput = document.querySelector("input[list=regions]"); //.value
const cityInputForCheck = document.querySelector("input[list=citys]"); //.value
const warehouseInput = document.querySelector("input[list=Warehouses]"); //.value

export async function sendFormToTelegram()  {
    event.preventDefault();

    const cartedItems =  getItemsFromStorageCart();
    const cartTitle = document.getElementById('cart-title');

    confirmOrderBtn.classList.add('loading');

    cartedItems.forEach(item => {
        if (item.size == "Не обрано") {
        // console.log("TEST", item.size)
        event.preventDefault(); 
        const errorMessageCart = document.querySelector('.error-message-cart');
        errorMessageCart.style.display = 'block';

        cartTitle.insertAdjacentElement('afterend', errorMessageCart); 
        }
    });

    const isFormValid = nameInput.value.trim() !== '' &&
                        secondNameInput.value.trim() !== '' &&
                        fatherNameInput.value.trim() !== '' &&
                        emailInput.value.trim() !== '' &&
                        phoneInput.value.trim() !== '' &&
                        oblastInput.value.trim() !== '' &&
                        cityInputForCheck.value.trim() !== '' && 
                        warehouseInput.value.trim() !== '' &&
                        methodCheckbox.checked &&
                        !cartedItems.some(item => item.size === "Не обрано");

    if (!isFormValid) {
        event.preventDefault();
        confirmOrderBtn.classList.remove('loading');
        if (fatherNameInput.value.trim() === '') {
        fatherNameInput.classList.add('error');
        }

        if (nameInput.value.trim() === '') {
        nameInput.classList.add('error');
        }

        if (oblastInput.value.trim() === '') {
        oblastInput.classList.add('error');
        }

        if (cityInputForCheck.value.trim() === '') {
        cityInputForCheck.classList.add('error');
        }

        if (warehouseInput.value.trim() === '') {
        warehouseInput.classList.add('error');
        }

        if (!methodCheckbox.checked){
        methodCheckboxText.classList.add('error-checkbox-text');
        }

        if (secondNameInput.value.trim() === '') {
        secondNameInput.classList.add('error');
        }

        if (emailInput.value.trim() === '') {
        emailInput.classList.add('error');
        }

        if (phoneInput.value.trim() === '') {
        phoneInput.classList.add('error');
        }

        return
    }

    const nameTELEGRAM = document.getElementById("name-input").value;
    const secondNameTELEGRAM = document.getElementById("second-name-input").value;
    const fatherNameTELEGRAM = document.getElementById("father-name-input").value;
    const emailTELEGRAM = document.getElementById("email-input").value;
    const phoneTELEGRAM = document.getElementById("phone-input").value;
    const commentTELEGRAM = document.querySelector("textarea").value;
    const regionTELEGRAM = document.getElementById("region-input").value;
    const cityTELEGRAM = document.getElementById("city-input").value;
    const warehouseTELEGRAM = document.getElementById("Warehouse-input").value;
    const totalTELEGRAM = document.querySelector(".total-price-valye");

    const paymentMethodTELEGRAM = document.getElementById("method-checkbox").checked ? "Накладний платіж" : "Повна оплата";

    const cartItemPaymentContainerTELEFRAM = document.querySelector(".cart-item-payment-container");

    const goodNameTELEGRAM = Array.from(cartItemPaymentContainerTELEFRAM.querySelectorAll(".InfoMainTextElement")).map(item => item.textContent)

    const InfoMainCodeElementValueTELEGRAM = Array.from(cartItemPaymentContainerTELEFRAM.querySelectorAll(".InfoMainCodeElementValue")).map(item => item.textContent)

    const InfoMainSizeElementValueTELEGRAM = Array.from(cartItemPaymentContainerTELEFRAM.querySelectorAll(".InfoMainSizeElementValuePayment")).map(select => select.value);

    const InfoColorMainElementValueTELEGRAM = Array.from(cartItemPaymentContainerTELEFRAM.querySelectorAll(".InfoColorMainElementValue")).map(item => item.textContent)

    const InfoPriceColorElementTELEGRAM = Array.from(cartItemPaymentContainerTELEFRAM.querySelectorAll(".InfoPriceColorElement")).map(item => item.textContent)

    const goodsToBuyTELEGRAM = []

    goodNameTELEGRAM.forEach((goodName, index) => {
        goodsToBuyTELEGRAM.push({
        name: goodName,
        code: InfoMainCodeElementValueTELEGRAM[index],
        size: InfoMainSizeElementValueTELEGRAM[index],
        color: InfoColorMainElementValueTELEGRAM[index],
        price: InfoPriceColorElementTELEGRAM[index],
        });
    });

    const orderData = {
        nameTELEGRAM,
        secondNameTELEGRAM,
        fatherNameTELEGRAM,
        emailTELEGRAM,
        phoneTELEGRAM,
        commentTELEGRAM,
        regionTELEGRAM,
        cityTELEGRAM,
        warehouseTELEGRAM,
        paymentMethodTELEGRAM,
        goodsToBuyTELEGRAM,
        totalTELEGRAM,
    };

    try {
        const response = await fetch("/new_order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(orderData),
        });

        const result = await response.json();
        if (result.status === "success") {
        showModal("Замовлення успішно відправлене!");
        for (const key of Object.keys(localStorage)) {
            if (key.includes("cart")) {
            localStorage.removeItem(key);
            }
        }
        } else {
        showModal("Помилка при відправці замовлення: " + result.message);
        }
    } catch (error) {
        showModal("Сталася помилка: " + error.message);
    } finally {
        confirmOrderBtn.classList.remove('loading');
    }
}
window.sendFormToTelegram = sendFormToTelegram; 