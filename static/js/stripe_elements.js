    let publicKeyElement = document.querySelector('#id_stripe_public_key');
    let clientSecretElement = document.querySelector('#id_client_secret');

    let stripe_public_key = publicKeyElement.textContent.slice(1, -1);
    let client_secret = clientSecretElement.textContent.slice(1, -1);

    let stripe = Stripe(stripe_public_key);
    let elements = stripe.elements();
    var card = elements.create("card");
    card.mount('#card-element');