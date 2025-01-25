export function toggleCare() {
    const care = document.querySelector(".composition-and-care");
    const description = document.querySelector(".description");

    if (care) {
        if (care.classList.contains("closeCare")) {
            care.style.maxHeight = care.scrollHeight + "px";

            // Якщо description відкритий, закриваємо його
            if (!description.classList.contains("closeDescription")) {
                description.classList.add("closeDescription");
                description.style.maxHeight = "40px"; // Закриваємо description
            }
        } else {
            // Згортаємо care
            care.style.maxHeight = "40px";
        }

        care.classList.toggle("closeCare");
    }
}
window.toggleCare = toggleCare;