import {getCityInOblast} from '../getCityInOblast.js'

export async function populateCitys(RefOblast, InputByUser_City) {
    const citys = await getCityInOblast(RefOblast, InputByUser_City);
    const dataListOnPage = document.getElementById('citys');

    const existingOptions = new Set(
        Array.from(dataListOnPage.options).map(option => option.value)
    );

    for (const citysName in citys) {
        if (!existingOptions.has(citysName)) { 
        const option = document.createElement('option');
        option.value = citysName;
        option.dataset.ref = citys[citysName];
        dataListOnPage.appendChild(option);
        }
    }
}
window.populateCitys = populateCitys;  