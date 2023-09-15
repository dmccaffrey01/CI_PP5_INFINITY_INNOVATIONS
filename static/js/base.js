const headerDropdownHeadings = document.querySelectorAll(".bottom-header-dropdown-heading");
const headerDropdownContainers = document.querySelectorAll(".bottom-header-dropdown-container");
const bottomHeaderContainer = document.querySelector(".bottom-header-container");


const removeActiveDropdown = (i) => {
    headerDropdownContainers.forEach((container, k) => {
        if (k !== i && container.classList.contains("active")) {
            container.classList.remove("active");
        }
    });
}

headerDropdownHeadings.forEach((heading, index) => {
    heading.addEventListener("mouseenter", () => {
        removeActiveDropdown(index);
        headerDropdownContainers[index].classList.add("active");

        bottomHeaderContainer.addEventListener("mouseleave", () => {
            removeActiveDropdown(-1);
        });
    });
});