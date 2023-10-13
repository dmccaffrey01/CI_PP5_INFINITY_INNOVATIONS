// Handle quantity button clicks
const incrementBtns = document.querySelectorAll(".increment-qty");
const decrementBtns = document.querySelectorAll(".decrement-qty");
const allQtyInputs = document.querySelectorAll(".qty_input");

const handleEnableDisable = (itemId) => {
    let inputSelector = "#id_qty_" + itemId;
    let currentInput = document.querySelector(inputSelector);
    let currentValue = parseInt(currentInput.value);

    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 98;

    let decrementSelector = "#decrement-qty_" + itemId;
    let incrementSelector = "#increment-qty_" + itemId;
    let decrementBtn = document.querySelector(decrementSelector);
    let incrementBtn = document.querySelector(incrementSelector);

    decrementBtn.disabled = minusDisabled;
    incrementBtn.disabled = plusDisabled;
};

allQtyInputs.forEach((input) => {
    let itemId = input.getAttribute("data-item_id");
    handleEnableDisable(itemId);

    input.addEventListener("change", () => {
        handleEnableDisable(itemId);
    });
});

incrementBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        let closestInput = btn.parentElement.querySelector(".atc-input");
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue + 1;
        let itemId = btn.getAttribute("data-item_id");
        handleEnableDisable(itemId);
    });
});

decrementBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        let closestInput = btn.parentElement.querySelector(".atc-input");
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue - 1;
        let itemId = btn.getAttribute("data-item_id");
        handleEnableDisable(itemId);
    });
});

const updateQtyBtns = document.querySelectorAll(".update-qty-btn");
const removeItemBtns = document.querySelectorAll(".remove-item-btn");

updateQtyBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        let form = btn.parentElement.parentElement.querySelector(".update-qty-form");
        form.submit();
    });
});

removeItemBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        let csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        let itemId = btn.getAttribute("id").split("remove_")[1];
        let theme = btn.getAttribute("data-product_theme");

        let form = new FormData();
        form.append("csrfmiddlewaretoken", csrfToken);
        form.append("product_theme", theme);

        let url = `/cart/remove/${itemId}/`;

        fetch(url, {
            method: "POST",
            body: form,
        })
        .then(() => {
            location.reload();
        });
    });
});
    
