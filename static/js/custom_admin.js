document.addEventListener("DOMContentLoaded", () => {
    const selectLinks = document.querySelectorAll(".admin-home-card-open-select");

    selectLinks.forEach((link) => {
        link.addEventListener("click", () => {
            let homeCard = link.parentNode;

            /* Open Select */

            let selectContainer = homeCard.querySelector(".admin-home-card-select-container");
            let selectOverlay = homeCard.querySelector(".admin-home-card-select-overlay");

            selectContainer.style.display = "flex";
            selectOverlay.style.display = "flex";

            /* Close Select */

            let closeBtn = homeCard.querySelector(".admin-home-card-select-close-btn");

            closeBtn.addEventListener("click", () => {
                selectContainer.style.display = "none";
                selectOverlay.style.display = "none";
            });

            /* Handle Search Input */

            const searchInput = homeCard.querySelector(".admin-home-card-select-search-input");

            const searchIcon = homeCard.querySelector(".search-input-search-icon");
            const closeIcon = homeCard.querySelector(".search-input-close-icon");

            const selectItemsContainer = homeCard.querySelector(".admin-home-card-select-items-container ");
            const removedSelectItems = homeCard.querySelectorAll(".admin-home-card-select-item-container");
            let removedSelectItemsArr = [];
            let currentSelectItems = Array.from(removedSelectItems);

            const handleInput = () => {
                const query = searchInput.value.toLowerCase();
                let removedSelectItems = [];
                let workingSelectItems = [];
                for (let i = 0; i < currentSelectItems.length; i++) {
                    const selectItem = currentSelectItems[i];
                    const name = selectItem.getAttribute("data-name").toLowerCase();

                    if (name.includes(query)) {
                        workingSelectItems.push(selectItem);
                    } else if (query.length != removedSelectItemsArr.length) {
                        removedSelectItems.push({"itemElement": selectItem, "index": i});
                    }
                }
                currentSelectItems = workingSelectItems;
                if (query.length != removedSelectItemsArr.length) {
                    removedSelectItemsArr.push(removedSelectItems);
                }
                for (let i = 0; i < removedSelectItems.length; i++) {
                    let selectItem = removedSelectItems[i].itemElement;
                    selectItem.remove();
                }
            }

            const addLastRemovedSelectItems = () => {
                let removedSelectItems = removedSelectItemsArr.pop();
                for (let i = 0; i < removedSelectItems.length; i++) {
                    let selectItem = removedSelectItems[i];
                    let itemElement = selectItem.itemElement;
                    let itemIndex = selectItem.index;
                    currentSelectItems.splice(itemIndex, 0, itemElement);
                    let siblingItem = selectItemsContainer.children[itemIndex];
                    selectItemsContainer.insertBefore(itemElement, siblingItem);
                }
                setTimeout(() => {
                    handleInput();
                }, 0);
            }

            const addAllRemovedSelectItems = () => {
                while(removedSelectItemsArr.length != 0) {
                    addLastRemovedSelectItems();
                }
            }

            const handleBackspaceInput = () => {
                addLastRemovedSelectItems();
            }

            searchInput.addEventListener("input", handleInput);

            searchInput.addEventListener("keydown", (event) => {
                if (event.key === "Backspace" || event.keyCode === 8) {
                    handleBackspaceInput();
                }
            });


            closeIcon.addEventListener("click", () => {
                searchInput.value = "";
                closeIcon.classList.remove("search");
                searchIcon.classList.remove("search");
                searchInput.classList.remove("search");
                addAllRemovedSelectItems();
            });

            searchInput.addEventListener("focus", () => {
                closeIcon.classList.add("search");
                searchIcon.classList.add("search");
                searchInput.classList.add("search");
            });

            /* Handle Select Button */

            const action = link.getAttribute("data-action");
            const modelType = link.getAttribute("data-model-type");

            const selectBtn = homeCard.querySelector(".admin-home-card-select-btn");

            const selectItems = homeCard.querySelectorAll(".admin-home-card-select-item-container");

            const removeOtherSelected = (i) => {
                selectItems.forEach((selectItem, k) => {
                    if (selectItem.classList.contains("selected") && k != i) {
                        selectItem.classList.remove("selected");
                    }
                });
            }

            selectItems.forEach((selectItem, i) => {
                selectItem.addEventListener("click", () => {
                    if (selectItem.classList.contains("selected")) {
                        selectItem.classList.remove("selected");

                        removeOtherSelected(i);
                    } else {
                        selectItem.classList.add("selected");
                    }

                });
            });

            const displayPopup = (message, url) => {
                const notificationContainer = document.querySelector('.admin-home-select-notification-container');

                let messageElement = notificationContainer.querySelector('.admin-home-select-popup-message');

                messageElement.innerHTML = message;


                let popupCancelBtn = notificationContainer.querySelector(".admin-home-select-popup-cancel-btn");
                let confirmBtn = notificationContainer.querySelector(".admin-home-select-popup-confirm-btn");

                popupCancelBtn.addEventListener("click", () => {
                    notificationContainer.style.display = 'none';
                });

                confirmBtn.addEventListener("click", () => {
                    window.location.replace(url);
                });

                notificationContainer.style.display = 'flex';

                let popupCloseBtn = notificationContainer.querySelector(".admin-home-select-popup-close-btn");

                popupCloseBtn.addEventListener("click", () => {
                    notificationContainer.style.display = 'none';
                });
            }

            const getSelectedId = () => {
                let id;

                selectItems.forEach((selectItem) => {
                    if (selectItem.classList.contains("selected")) {
                        id = selectItem.getAttribute("data-id");
                    }
                });

                return id
            }

            const handleSelectBtn = () => {
                let selectedId = getSelectedId()
                
                let currentUrl = new URL(window.location);

                currentUrl.pathname += `${modelType}/${action}/${selectedId}`;

                if (action == "delete") {
                    displayPopup("Are you sure you want to delete the selected item?", currentUrl);
                } else {
                    window.location.replace(currentUrl);
                }
            }

            selectBtn.addEventListener("click", handleSelectBtn);

        });
    });
});

