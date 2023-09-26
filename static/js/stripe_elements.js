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

    let saveInfoElement = document.querySelector('#id-save-info');
    let saveInfo = Boolean(saveInfoElement.getAttribute('checked'));
    let csrfTokenElement = document.querySelector('input[name="csrfmiddlewaretoken"]');
    let csrfToken = csrfTokenElement.value;
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(() => {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                }
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
    }).fail(error => {
        // Reaload the page
        location.reload();
    });
});