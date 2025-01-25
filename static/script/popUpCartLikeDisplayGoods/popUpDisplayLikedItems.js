import {getItemsFromStorage} from '../localStorageGetItemsCartLike/getItemsFromStorageLike.js'

export function displayLikedItems() {
    const likedItems = getItemsFromStorage();
    const likedGoodsContainer = document.querySelector('.likedGoodsContainer');

    likedGoodsContainer.innerHTML = '';

    if (likedItems.length === 0) {
        likedGoodsContainer.innerHTML = '<div class="likedGoodsContainerTitleNotFound">Іди, шось перше но полайкай</div>';
        return;
    }

    likedItems.forEach(item => {

        const wrapperImgElement = document.createElement('div');
        wrapperImgElement.classList.add('likedGoodsContainerImageWraper');

        const imgElement = document.createElement('img');
        imgElement.src = item.src; 
        imgElement.alt = 'liked good image'; 
        imgElement.classList.add('likedGoodsContainerImage');

        wrapperImgElement.appendChild(imgElement);

        const wrapperInfoElement = document.createElement('div');
        wrapperInfoElement.classList.add('likedGoodsContainerInfoWraper');

        const InfoMainTextElement = document.createElement('a');
        InfoMainTextElement.classList.add('InfoMainTextElement');
        InfoMainTextElement.href = `${baseGoodUrl}${item.id}`;
        InfoMainTextElement.textContent = item.name;
        wrapperInfoElement.appendChild(InfoMainTextElement);

        const wrapperContentElement = document.createElement('div');
        wrapperContentElement.classList.add('likedGoodsContentElement');

        wrapperContentElement.appendChild(wrapperImgElement);
        wrapperContentElement.appendChild(wrapperInfoElement);

        likedGoodsContainer.appendChild(wrapperContentElement);

        const InfoMainCodeElement = document.createElement('h2');
        InfoMainCodeElement.classList.add('InfoMainCodeElement');
        InfoMainCodeElement.innerHTML = `<div class="InfoMainElementWraper">
            <span class="InfoMainCodeElementLabel">Артикул:</span> 
            <span class="InfoMainCodeElementValue">${item.code}</span>
        </div>`;
        wrapperInfoElement.appendChild(InfoMainCodeElement);

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
        toggleLike(item.id);
        };
        wrapperInfoElement.appendChild(InfoElementDeleteButton);
    });
}
window.displayLikedItems = displayLikedItems;