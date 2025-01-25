export function toggleVisibility(activeElement, inactiveElement) {

    const inactive = document.querySelector(inactiveElement);

    if (inactive.classList.contains('show')){
      inactive.classList.add('close'); 
    }

    const active = document.querySelector(activeElement);

    if (inactive.classList.contains('close')) {
      active.classList.add('show'); 
    }
}
window.toggleVisibility = toggleVisibility;