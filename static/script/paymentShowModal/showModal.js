export function showModal(message) {
    const succeed = document.querySelector(".succeed-payment-container");
    const succeedMessage = document.querySelector(".succeed-payment-message");
    const succeedModal = document.querySelector(".succeed-payment-close");

    succeedMessage.textContent = message;
    succeed.style.display = "block";

    succeedModal.onclick = function () {
        window.location.href = "/";
    };
}
window.showModal = showModal;  