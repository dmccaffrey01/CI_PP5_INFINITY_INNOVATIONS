// Filter select dropdown change
const updateFilterURL = (valueElement, type) => {
    let selectedVal = valueElement.getAttribute("data-select-value");

    if (type == "sort") {
        let currentUrl = new URL(window.location);

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
    } else if (type == "universe") {
        let currentUrl = new URL(window.location.href);
        let splitUrl = currentUrl.pathname.split("/");
        splitUrl.pop();
        
        if ((splitUrl.slice(-1)[0] == "real" || splitUrl.slice(-1)[0] == "digital") && splitUrl.slice(-2, -1)[0] == "products") {
            splitUrl.pop();
        }
        if (selectedVal != "reset") {
            splitUrl.push(selectedVal);
            if (currentUrl.searchParams.has("category")) {
                currentUrl.searchParams.delete("category");
            }
            if (currentUrl.searchParams.has("brand")) {
                currentUrl.searchParams.delete("brand");
            }
        }
            
        currentUrl.pathname = splitUrl.join("/");
        currentUrl.pathname = currentUrl.pathname + "/";
        window.location.replace(currentUrl);

    } else if (type == "category") {
        let currentUrl = new URL(window.location.href);

        if (selectedVal != "reset") {
            if (currentUrl.searchParams.has("category")) {
                let existingCategories = currentUrl.searchParams.get("category");
                let splitCategories = existingCategories.split(",");

                let indexOfSelectedVal = splitCategories.indexOf(selectedVal);
                if (indexOfSelectedVal !== -1) {
                    splitCategories.splice(indexOfSelectedVal, 1);

                    let remainingCategories = splitCategories.join(",");
                    if (remainingCategories) {
                        currentUrl.searchParams.set("category", remainingCategories);
                    } else {
                        currentUrl.searchParams.delete("category");
                    }
                } else {
                    currentUrl.searchParams.set("category", existingCategories + "," + selectedVal);
                }
            } else {
                currentUrl.searchParams.set("category", selectedVal);
            }

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("category");

            window.location.replace(currentUrl);
        }
    } else if (type == "brand") {
        let currentUrl = new URL(window.location.href);

        if (selectedVal != "reset") {
            if (currentUrl.searchParams.has("brand")) {
                let existingBrands = currentUrl.searchParams.get("brand");
                let splitBrands = existingBrands.split(",");

                let indexOfSelectedVal = splitBrands.indexOf(selectedVal);
                if (indexOfSelectedVal !== -1) {
                    splitBrands.splice(indexOfSelectedVal, 1);

                    let remainingBrands = splitBrands.join(",");
                    if (remainingBrands) {
                        currentUrl.searchParams.set("brand", remainingBrands);
                    } else {
                        currentUrl.searchParams.delete("brand");
                    }
                } else {
                    currentUrl.searchParams.set("brand", existingBrands + "," + selectedVal);
                }
            } else {
                currentUrl.searchParams.set("brand", selectedVal);
            }

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("brand");

            window.location.replace(currentUrl);
        }
    }
};

const closeFilterDropdown = (selector) => {
    selector.classList.remove("active");
    
    let dropdown = selector.querySelector(".custom-select-filter-dropdown-container");

    dropdown.style.display = "none";

    let icon = selector.querySelector(".fa-chevron-down");

    icon.style.transform = "rotate(0deg)";
};

const openFilterDropdown = (selector, type) => {
    selector.classList.add("active");
    
    let dropdown = selector.querySelector(".custom-select-filter-dropdown-container");

    dropdown.style.display = "flex";

    let icon = selector.querySelector(".fa-chevron-down");

    icon.style.transform = "rotate(-180deg)";

    let dropdownValues = dropdown.querySelectorAll(".dropdown-value");

    dropdownValues.forEach((value) => {
        value.addEventListener("click", () => {
            updateFilterURL(value, type);
            closeFilterDropdown(selector);
        });
    });
};

const filterSelectors = document.querySelectorAll(".custom-select-filter-container");

filterSelectors.forEach((selector) => {
    let type = selector.getAttribute("data-filter-type");
    
    selector.addEventListener("click", () => {
        if (selector.classList.contains("active")) {
            closeFilterDropdown(selector);
        } else {
            openFilterDropdown(selector, type);
        }
        
    });
});
