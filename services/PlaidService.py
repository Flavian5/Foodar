"""Service class: wrapper for Plaid connection"""

import plaid
from flask import jsonify


class PlaidService():

    PLAID_CLIENT_ID = 'CLIENT_ID'
    PLAID_SECRET = 'SECRET'
    PLAID_PUBLIC_KEY = 'PUBLIC_KEY'
    PLAID_ENV = 'sandbox'
    PLAID_PRODUCTS = ['auth', 'transactions']

    client = plaid.Client('PLAID_CLIENT_ID',
                          'PLAID_SECRET',
                          'PLAID_PUBLIC_KEY',
                          'sandbox')

    def get_account_info(self, public_token):
        exchange_response = self.client.Item.public_token.exchange(public_token)
        access_token = exchange_response['access_token']
        auth_response = self.client.Auth.get(access_token)
        return jsonify({'error': None, 'auth': auth_response})
