# Checkout Process

1. Cart -> Checkout View
    ?
    - Login/Register or Enter an Email (as Guest)
    - Shipping Address
    - Billing Info
        - Billing Address
        - Credit Card / Payment

2. Billing App/Component
    - Billing Profile
        - User or Email (Guest Email)
        - generate payment processor token (Stripe or Braintree)

3. Orders / Invoices Components
    - Connect
        - Billing Profile
        - Shipping / Billing
        - Cart
        - Status --Shipped? or Cancelled?
