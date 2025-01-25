let abortController;
export async function populateHouses(nameCity, InputByUser_House) {
    if (abortController) {
        abortController.abort();
    }
    abortController = new AbortController();
    const signal = abortController.signal;

    try {
        const houses = await getHousesInCity(nameCity, InputByUser_House, { signal });

        const dataListOnPage = document.getElementById('Warehouses');

        dataListOnPage.innerHTML = "";

        for (const housesName in houses) {
            const option = document.createElement('option');
            option.value = housesName;
            option.dataset.ref = houses[housesName];
            dataListOnPage.appendChild(option);
        }
    } catch (error) {
        if (error.name === 'AbortError') {
            console.log('Previous request aborted');
        } else {
            console.error('Error fetching houses:', error);
        }
    }
}

window.populateHouses = populateHouses;  