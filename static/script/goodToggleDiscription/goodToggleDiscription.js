export function toggleDescription() {
    const description = document.querySelector(".description");
    const care = document.querySelector(".composition-and-care");

    if (description) {
        if (description.classList.contains("closeDescription")) {
            description.style.maxHeight = description.scrollHeight + "px"; 

            if (!care.classList.contains("closeCare")) {
                care.classList.add("closeCare");
                care.style.maxHeight = "40px";
            }
        } else {
            description.style.maxHeight = "40px";
        }

        description.classList.toggle("closeDescription");
    }
}

window.toggleDescription = toggleDescription;