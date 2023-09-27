const sortFilterSelector = document.querySelector("#sort-filter-selector");

const updateFilterURL = (valueElement, type) => {
    let currentUrl = new URL(window.location);

    let selectedVal = valueElement.getAttribute("data-select-value");

    if (type == "sort") {

        if (selectedVal != "reset") {
            let sort = selectedVal.split("_")[0];
            let direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    }
}

const closeFilterDropdown = (selector) => {
    selector.classList.remove("active");
    
    let dropdown = selector.querySelector(".custom-select-filter-dropdown-container");

    dropdown.style.display = "none";

    let icon = selector.querySelector(".fa-chevron-down");

    icon.style.transform = "rotate(0deg)";
}

const openFilterDropdown = (selector) => {
    selector.classList.add("active");
    
    let dropdown = selector.querySelector(".custom-select-filter-dropdown-container");

    dropdown.style.display = "flex";

    let icon = selector.querySelector(".fa-chevron-down");

    icon.style.transform = "rotate(-180deg)";

    let dropdownValues = dropdown.querySelectorAll(".dropdown-value");

    dropdownValues.forEach((value) => {
        value.addEventListener("click", () => {
            updateFilterURL(value, "sort");
            closeFilterDropdown(selector);
        });
    });
}

sortFilterSelector.addEventListener("click", () => {
    if (sortFilterSelector.classList.contains("active")) {
        closeFilterDropdown(sortFilterSelector);
    } else {
        openFilterDropdown(sortFilterSelector);
    }
    
});