import {listOfOblasts} from '../index.js'

export async function getOblast() {
    try {
        const response = await fetch('/get_oblast');
        if (!response.ok) {
            throw new Error('Failed to fetch oblast data');
        }

        const getOblast = await response.json();

        getOblast.forEach(item => {
        listOfOblasts[item.Description] = item.Ref
        })

        return listOfOblasts
    } catch (error) {
        console.error("Error fetching oblast data:", error);
    }
}
window.getOblast = getOblast;  