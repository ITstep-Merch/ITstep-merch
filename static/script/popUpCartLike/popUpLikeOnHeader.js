export function toggleDropdownLike() {
  const dropdown = document.querySelector('.likeDropdownChild');
  if (dropdown.classList.contains('show')) {
      dropdown.classList.add('close');
      dropdown.classList.remove('show');
      // dropdown.classList.remove('close');
      setTimeout(() => {
          dropdown.classList.remove('close');
      }, 300); 
  } else {
      dropdown.classList.add('show');
  }
}
window.toggleDropdownLike = toggleDropdownLike;