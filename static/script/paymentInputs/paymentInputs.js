const nameInput = document.getElementById('name-input');
const secondNameInput = document.getElementById('second-name-input');
const fatherNameInput = document.getElementById('father-name-input');
const emailInput = document.getElementById('email-input');
const phoneInput = document.getElementById('phone-input');
const methodCheckboxText = document.getElementById('method-checkbox-text');
const methodCheckbox = document.getElementById('method-checkbox');
const oblastInput = document.querySelector("input[list=regions]"); //.value
const cityInputForCheck = document.querySelector("input[list=citys]"); //.value
const warehouseInput = document.querySelector("input[list=Warehouses]"); //.value

export function paymentInputs(){

    nameInput.addEventListener('input', () => {
        if (nameInput.value.trim() !== '') {
            nameInput.classList.remove('error'); 
        } else {
            nameInput.classList.add('error');
        }
    });

    secondNameInput.addEventListener('input', () => {
        if (secondNameInput.value.trim() !== '') {
        secondNameInput.classList.remove('error'); 
        } else {
        secondNameInput.classList.add('error');
        }
    });

    fatherNameInput.addEventListener('input', () => {
        if (fatherNameInput.value.trim() !== '') {
        fatherNameInput.classList.remove('error'); 
        } else {
        fatherNameInput.classList.add('error');
        }
    });

    emailInput.addEventListener('input', () => {
        if (emailInput.value.trim() !== '') {
        emailInput.classList.remove('error'); 
        } else {
        emailInput.classList.add('error');
        }
    });

    phoneInput.addEventListener('input', () => {
        if (phoneInput.value.trim() !== '') {
        phoneInput.classList.remove('error'); 
        } else {
        phoneInput.classList.add('error');
        }
    });

    methodCheckboxText.addEventListener('input', () => {
        if (!methodCheckbox.checked) {
        methodCheckboxText.classList.add('error-checkbox-text'); 
        } else {
        methodCheckboxText.classList.remove('error-checkbox-text');
        }
    });

    oblastInput.addEventListener('input', () => {
        if (oblastInput.value.trim() !== '') {
        oblastInput.classList.remove('error'); 
        } else {
        oblastInput.classList.add('error'); 
        }
    });

    cityInputForCheck.addEventListener('input', () => {
        if (cityInputForCheck.value.trim() !== '') {
        cityInputForCheck.classList.remove('error'); 
        } else {
        cityInputForCheck.classList.add('error'); 
        }
    });

    warehouseInput.addEventListener('input', () => {
        if (warehouseInput.value.trim() !== '') {
        warehouseInput.classList.remove('error'); 
        } else {
        warehouseInput.classList.add('error'); 
        }
    });
}
window.paymentInputs = paymentInputs;


