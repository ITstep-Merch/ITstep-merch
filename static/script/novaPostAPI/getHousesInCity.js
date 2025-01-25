export async function getHousesInCity(nameCity, InputByUser_House) {
    try {
        const response = await fetch(`/get_wareHouse_in_city_streetAd?nameCity=${nameCity}&InputByUser_House=${InputByUser_House}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
        });
        if (!response.ok) {
            throw new Error('Failed to fetch city data');
        }

        const getHouseInCity = await response.json();
        let listOfHousesInCity = {}

        getHouseInCity.forEach(item => {
            listOfHousesInCity[item.Description] = item.Ref
        })

        return listOfHousesInCity
    } catch (error) {
        console.error("Error fetching oblast data:", error);
    }
}
window.getHousesInCity = getHousesInCity;  