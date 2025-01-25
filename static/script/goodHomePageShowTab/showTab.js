export function showTab(tabId) {
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });

    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.add('hidden');
    });

    document.getElementById(tabId).classList.remove('hidden');
    document.querySelector(`.tab-button[onclick="showTab('${tabId}')"]`).classList.add('active');
}
window.showTab = showTab;