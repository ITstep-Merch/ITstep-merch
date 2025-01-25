import {getOblast} from '../getOblas.js'

export async function populateRegions() {
    const regions = await getOblast();

    for (const regionName in regions) {
    const option = document.createElement('option');
    option.value = regionName;
    option.dataset.ref = regions[regionName];
    document.getElementById('regions').appendChild(option);
    }
}
window.populateRegions = populateRegions;  