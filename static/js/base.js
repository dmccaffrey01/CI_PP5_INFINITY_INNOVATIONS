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
const accountWrapper = document.querySelector(".account-header-dropdown-wrapper");
const cartHeader = document.querySelector(".cart-header-container");
const cartDropdownContainer = document.querySelector(".cart-header-dropdown-container");
const cartWrapper = document.querySelector(".cart-header-dropdown-wrapper");

accountHeader.addEventListener("mouseenter", () => {
    cartDropdownContainer.style.display = "none";
    cartWrapper.style.transform = "translateY(-100%)";
    
    accountDropdownContainer.style.display = "flex";
    accountWrapper.style.transform = "translateY(-80%)";
    window.setTimeout(() => {
        accountWrapper.style.transform = "translateY(0%)";
    }, 10)

    accountHeader.addEventListener("mouseleave", () => {
        accountWrapper.style.transform = "translateY(-100%)"
        window.setTimeout(() => {
            accountDropdownContainer.style.display = "none";
        }, 100);
    });
});

cartHeader.addEventListener("mouseenter", () => {
    accountDropdownContainer.style.display = "none";
    accountWrapper.style.transform = "translateY(-100%)";
    
    cartDropdownContainer.style.display = "flex";
    cartWrapper.style.transform = "translateY(-80%)";
    window.setTimeout(() => {
        cartWrapper.style.transform = "translateY(0%)";
    }, 10)

    accountCartContainer.addEventListener("mouseleave", () => {
        cartWrapper.style.transform = "translateY(-100%)";
        window.setTimeout(() => {
            cartDropdownContainer.style.display = "none";
        }, 100);
    });
});

// cartHeader.addEventListener("click", () => {
//     window.location.href = '/cart/';
// });