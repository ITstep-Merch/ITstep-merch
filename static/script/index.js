import {toggleVisibility} from './popUpCartLike/popUpVisibilityOnHeader.js'
import {toggleDropdownLike} from './popUpCartLike/popUpLikeOnHeader.js'
import {toggleDropdownCart} from './popUpCartLike/popUpCartOnHeader.js'

import {displayCartedItems} from './popUpCartLikeDisplayGoods/popUpDisplayCartedItems.js'
import {displayLikedItems} from './popUpCartLikeDisplayGoods/popUpDisplayLikedItems.js'

import {initializeLikesCounter} from './popUpCartLikeInitializeCounter/popUpinitializeLikesCouner.js'
import {initializeCartsCounter} from './popUpCartLikeInitializeCounter/popUpInitializeCartsCouner.js'

import {animateLike} from './goodHomePageAnimateCartLike/goodHomeAnimateLike.js'
import {animateCart} from './goodHomePageAnimateCartLike/goodHomeAnimateCart.js'

import {saveGoodToLocalStorage} from './localStorageSaveItemsCartLike/saveItemsToStorageLike.js'
import {saveGoodToLocalStorageCart} from './localStorageSaveItemsCartLike/saveItemsToStorageCart.js'

import {toggleLike} from './goodHomeToggleLikeCart/goodHomeToggleLike.js'
import {toggleCart} from './goodHomeToggleLikeCart/goodHomeToggleCart.js'
import {togglePayment} from './paymentToggle/togglePayment.js'

import {scrollToCatalog} from './homeScrollToCatalog/scrollToCatalog.js'

import {initializePaymentPageElement} from './paymentInitializeGoods/initializePaymentPageElement.js'

import {getOblast} from './novaPostAPI/getOblas.js'
import {getCityInOblast} from './novaPostAPI/getCityInOblast.js'
import {getHousesInCity} from './novaPostAPI/getHousesInCity.js'

import {sendFormToTelegram} from './sendMessageToTelegram/sendFormToTelegram.js'

import {totalPriceValye} from './paymentTotalPrice/totalPriceValye.js'
if (document.querySelector('.total-price-valye')) totalPriceValye();

import {populateRegions} from './novaPostAPI/paymentPopulateRegions/populateRegions.js'
if (document.getElementById('regions')) populateRegions();
import {populateCitys} from './novaPostAPI/paymentPopulateRegions/populateCitys.js'
import {populateHouses} from './novaPostAPI/paymentPopulateRegions/populateHouses.js'

import {paymentInputs} from './paymentInputs/paymentInputs.js'

import {showModal} from './paymentShowModal/showModal.js'
import {showTab} from './goodHomePageShowTab/showTab.js'

import {meterOverlay} from './goodHomePageMeterOverlay/meterOverlay.js'

import {toggleDescription} from './goodToggleDiscription/goodToggleDiscription.js'
import {toggleCare} from './goodToggleDiscription/goodToggleCare.js'
 
const myForm = document.getElementById('myForm');

export const stateCart = { cartCounterOnPage: 0, };

export const stateLike = { likeCounter: 0, };

export let listOfOblasts = {};

export let listOfCityInOblast = {};

if (myForm) {
    const regionInput = document.getElementById('region-input');
    const cityInput = document.getElementById('city-input');
    const houseInput = document.getElementById('Warehouse-input');
    let RefOblast = 0;
    myForm.addEventListener('submit', sendFormToTelegram);

    regionInput.addEventListener('input', function() {
        const selectedRegion = regionInput.value;
        const selectedCity = cityInput.value;
        RefOblast = listOfOblasts[selectedRegion]
        const InputByUser_City = selectedCity
        if (RefOblast) {
            populateCitys(RefOblast, InputByUser_City);
        }
    });

    cityInput.addEventListener('input', function() {
        const selectedRegion = regionInput.value;
        const selectedCity = cityInput.value;
        RefOblast = listOfOblasts[selectedRegion]
        const InputByUser_City = selectedCity
        if (RefOblast) {
            const InputByUser_House = " ";
            const cityInput = document.getElementById('city-input');
            const nameCity = InputByUser_City
            populateCitys(RefOblast, InputByUser_City);
            populateHouses(nameCity, InputByUser_House);
        }
    });

    houseInput.addEventListener('input', function() {
        const selectedHouse = houseInput.value;
        const cityInput = document.getElementById('city-input');
        const nameCity = cityInput.value;
        const InputByUser_House = selectedHouse
        if (nameCity || InputByUser_House) {
            populateHouses(nameCity, InputByUser_House);
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    initializeLikesCounter();
    initializeCartsCounter();
    displayLikedItems(); 
    displayCartedItems(); 
    if (myForm) {
        paymentInputs();
    }

    for (let i = 0; i < localStorage.length; i++) {
        const getKeys = localStorage.key(i);
        if (getKeys.startsWith('cart-')) {
            const item = JSON.parse(localStorage.getItem(getKeys) || "{}");
            const toCartAfterReload = document.getElementById(getKeys);
            if (item.option === "Cart" && toCartAfterReload) {
                toCartAfterReload.classList.add('carted');
            }
        }
    }

    for (let i = 0; i < localStorage.length; i++) {
        const getKeys = localStorage.key(i);
        if (!getKeys.startsWith('cart-')) {
            const item = JSON.parse(localStorage.getItem(getKeys) || "{}");
            const toLikeAfterReload = document.getElementById(getKeys);
            if (item.option === "Like" && toLikeAfterReload) {
                toLikeAfterReload.classList.add('liked');
            }
        }
    }
});

if (window.location.pathname.includes('payment')) {
    document.addEventListener('DOMContentLoaded', initializePaymentPageElement);
}

if (window.location.pathname.includes('good')) {
    document.addEventListener('DOMContentLoaded', meterOverlay);
}

// <!-- 
// пофіксити сітку, -очікуємо
// адаптація
// головний тект на головній сторінці
// головні фото на гоовній сторінці
// щоб опис та догляд згортались
// -->