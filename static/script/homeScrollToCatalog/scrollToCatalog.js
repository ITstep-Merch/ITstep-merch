export function scrollToCatalog(){
    event.preventDefault(); 
    document.getElementById('catalogTitle').scrollIntoView({
        behavior: 'smooth', 
        block: 'start' 
    });
}
window.scrollToCatalog = scrollToCatalog;  