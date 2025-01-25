import {listOfCityInOblast} from '../index.js'

export async function getCityInOblast(RefOblast, InputByUser_City) {
    try {
        const response = await fetch(`/get_city_in_oblast?RefOblast=${RefOblast}&InputByUser_City=${InputByUser_City}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch city data');
        }

        const getCityInOblast = await response.json();

        getCityInOblast.forEach(item => {
        listOfCityInOblast[item.Description] = item.Ref
        })

        return listOfCityInOblast
    } catch (error) {
        console.error("Error fetching oblast data:", error);
    }
}   
window.getCityInOblast = getCityInOblast;  