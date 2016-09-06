# package to mask our environment variables
import os
from flask import Flask, render_template, request
import stripe

# dictionary for stripe keys
stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

# route configurations for static templates
@app.route('/')
def index():
  return render_template('index.html', key=stripe_keys['publishable_key'])

# post route for payments
@app.route('/api/v1/charge', methods=['POST'])
def charge():
  # hard coded amount in cents
  price = 500

  # hard coded customer
  customer = stripe.Customer.create(
    email='test@test.com',
    source=request.form['stripeToken']
  )

  charge = stripe.Charge.create(
    customer=customer.id,
    amount=price,
    currency='usd',
    description='flask stripe demo charge'
  )

  return render_template('successful.html', amount=price)

if __name__ == '__main__':
  app.run(debug=True)
