const sortFilterSelector = document.querySelector("#sort-filter-selector");

sortFilterSelector.addEventListener("change", () => {
    let currentUrl = new URL(window.location);
    console.log(currentUrl);
    let selectedVal = sortFilterSelector.value;

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
});