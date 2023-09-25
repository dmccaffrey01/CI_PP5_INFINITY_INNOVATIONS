let publicKeyElement = document.querySelector('#id_stripe_public_key');
let clientSecretElement = document.querySelector('#id_client_secret');

let stripePublicKey = publicKeyElement.textContent.slice(1, -1);
let clientSecret = clientSecretElement.textContent.slice(1, -1);

let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let card = elements.create('card');
card.mount('#card-element');

// Handle realtime validation error on the card element

const errorDiv = document.getElementById('card-errors');

card.addEventListener('change', (event) => {
    if (event.error) {
        let html = `
            <div class="stripe-error-icon-container container-col">
                <i class="fas fa-times"></i>
            </div>
            <div class="stripe-error-message">${event.error.message}</div>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.innerHTML = "";
    }
});

// Toggle fade in or out

const fadeIn = (element, duration) => {
    element.style.opacity = 0;
    element.style.display = "flex";
    
    let intervals = duration / 10;
    let i = 0;

    let fadeInterval = window.setInterval(() => {
        if (i >= intervals - 1) {
            element.style.opacity = 1;
            clearInterval(fadeInterval);
        } else {
            element.style.opacity = (i / intervals);
            i++;
        }
    }, 10);
};

const fadeOut = (element, duration) => {
    element.style.opacity = 1;
    element.style.display = "flex";
    
    let intervals = duration / 10;
    let i = 0;

    let fadeInterval = window.setInterval(() => {
        if (i >= intervals - 1) {
            element.style.opacity = 0;
            element.style.display = "none";
            clearInterval(fadeInterval);
        } else {
            element.style.opacity = 1 - (i / intervals);
            i++;
        }
    }, 10);
};

// Handle form submit

var form = document.getElementById('payment-form');
var submitBtn = document.getElementById('submit-button');
const formWrapper = document.querySelector('.checkout-section-wrapper');
const loadingOverlay = document.querySelector('.loading-overlay');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    submitBtn.setAttribute('disabled', true);
    fadeIn(loadingOverlay, 100);
    fadeOut(formWrapper, 100);

    stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            }
    }).then(function(result) {
        if (result.error) {
            let html = `
                <div class="stripe-error-icon-container container-col">
                    <i class="fas fa-times"></i>
                </div>
                <div class="stripe-error-message">${result.error.message}</div>`;
            errorDiv.innerHTML = html;

            fadeOut(loadingOverlay, 100);
            fadeIn(formWrapper, 100);
            card.update({ 'disabled': false });
            submitBtn.setAttribute('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});