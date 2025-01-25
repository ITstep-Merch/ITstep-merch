export function meterOverlay() {
    const meterOverlay = document.querySelector('.meter-overlay');
    const meterTableContainer = document.querySelector('.meter-table-container');
    const meterTableCloseButton = document.querySelector('.meter-table-container-close-button');
    const meterShowButton = document.querySelector('.meter-for-body');

    if(meterShowButton){
      meterShowButton.addEventListener('click', () => {
        meterOverlay.style.display = 'block'; 
        meterTableContainer.style.display = 'block'; 
        document.body.classList.add('locked'); 
      });
    }

    if(meterTableCloseButton){
      meterTableCloseButton.addEventListener('click', () => {
        meterOverlay.style.display = 'none';
        meterTableContainer.style.display = 'none';
        document.body.classList.remove('locked'); 
      });
    }

    if(meterOverlay){
      meterOverlay.addEventListener('click', () => {
        meterOverlay.style.display = 'none';
        meterTableContainer.style.display = 'none';
        document.body.classList.remove('locked'); 
      });
    }
}
window.meterOverlay = meterOverlay;