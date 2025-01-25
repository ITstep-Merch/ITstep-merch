export function toggleDropdownCart() {
    const dropdown = document.querySelector('.cartDropdownChild');
    if (dropdown.classList.contains('show')) {
        dropdown.classList.add('close');
        dropdown.classList.remove('show');
        setTimeout(() => {
            dropdown.classList.remove('close');
        }, 300); 
    } else {
        dropdown.classList.add('show');
    }
}  
window.toggleDropdownCart = toggleDropdownCart;