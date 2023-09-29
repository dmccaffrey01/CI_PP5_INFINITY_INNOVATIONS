let notificationContainer = document.querySelector(".toast-notification-container");
let notificationMessage = document.querySelector(".notification-message");
let notificationClose = document.querySelector(".close-toast-btn");
let notificationClosed = true;

const fadeInFadeOut = (inOrOut) => {
    let startingOpacity;
    let endingOpacity;
    let opacityPosNeg;
    
    if (inOrOut === 'in') {
        startingOpacity = 0;
        endingOpacity = 1;
        opacityPosNeg = 1;
        notificationContainer.style.opacity = startingOpacity;
        notificationContainer.style.display = 'flex';
    } else {
        startingOpacity = 1;
        endingOpacity = 0;
        opacityPosNeg = -1;
    }

    let duration = 800;
    let counter = 0;
    let currentOpacity = startingOpacity;
    let step = duration / 10;

    let fadeInterval = window.setInterval(() => {
        if (counter >= (duration - 10)) {
            if (inOrOut === 'out') {
                notificationContainer.style.display = 'none';
            }
            notificationContainer.style.opacity = endingOpacity;
            clearInterval(fadeInterval);
        } else {
            currentOpacity += (1 / step) * opacityPosNeg;
            notificationContainer.style.opacity = currentOpacity;
            counter += 10;
        }
    }, 10);

}

const closeNotification = () => {
    fadeInFadeOut("out");
    notificationClosed = true;
}

const displayNotification = () => {
    fadeInFadeOut("in");

    notificationClosed = false;

    window.setTimeout(() => {
        if (notificationClosed) {
            return;
        } else {
            closeNotification();
        }
        
    }, 4000);
}

notificationClose.addEventListener("click", () => {
    closeNotification();
});

document.addEventListener("DOMContentLoaded", () => {
    displayNotification();
});