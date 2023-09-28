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
        currentUrl.pathname = currentUrl.pathname + "/"
        window.location.replace(currentUrl);

    } else if (type == "category") {
        let currentUrl = new URL(window.location.href);

        if (selectedVal != "reset") {
            if (currentUrl.searchParams.has("category")) {
                let existingCategory = currentUrl.searchParams.get("category");
                currentUrl.searchParams.set("category", existingCategory + "," + selectedVal);
                
            } else {
                currentUrl.searchParams.set("category", selectedVal);
            }

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("category");

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
}

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
