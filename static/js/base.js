const headerDropdownHeadings = document.querySelectorAll(".bottom-header-dropdown-heading");
const headerDropdownContainers = document.querySelectorAll(".bottom-header-dropdown-container");
const bottomHeaderContainer = document.querySelector(".bottom-header-container");


const removeActiveDropdown = (i) => {
    headerDropdownContainers.forEach((container, k) => {
        if (k !== i && container.classList.contains("active")) {
            container.classList.remove("active");
            headerDropdownHeadings[k].classList.remove("active");
        }
    });
}

headerDropdownHeadings.forEach((heading, index) => {
    heading.addEventListener("mouseenter", () => {
        removeActiveDropdown(index);
        headerDropdownContainers[index].classList.add("active");
        heading.classList.add("active");

        bottomHeaderContainer.addEventListener("mouseleave", () => {
            removeActiveDropdown(-1);
        });
    });
});

const accountHeader = document.querySelector(".account-header-container");
const accountCartContainer = document.querySelector(".account-cart-container");
const accountDropdownContainer = document.querySelector(".account-header-dropdown-container");
const cartHeader = document.querySelector(".cart-header-container");
const cartDropdownContainer = document.querySelector(".cart-header-dropdown-container");

accountHeader.addEventListener("mouseenter", () => {
    accountDropdownContainer.style.display = "flex";
    cartDropdownContainer.style.display = "none";

    accountHeader.addEventListener("mouseleave", () => {
        accountDropdownContainer.style.display = "none";
    });
});

cartHeader.addEventListener("mouseenter", () => {
    cartDropdownContainer.style.display = "flex";
    accountDropdownContainer.style.display = "none";

    accountCartContainer.addEventListener("mouseleave", () => {
        cartDropdownContainer.style.display = "none";
    });
});