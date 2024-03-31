import requests
from config import headers


def get_user_data(h=headers):
    return requests.get('https://5sim.biz/v1/user/profile', headers=h).json()


def get_order_history(h=headers, category='activation', limit=15, offset=0, order='id', reverse=True):
    params = (
        ('category', category),
        ('limit', limit),
        ('offset', offset),
        ('order', order),
        ('reverse', reverse),
    )
    return requests.get('https://5sim.biz/v1/user/orders', headers=h, params=params).json()


def get_payment_history(h=headers, limit=15, offset=0, order='id', reverse=True):
    params = (
        ('limit', limit),
        ('offset', offset),
        ('order', order),
        ('reverse', reverse),
    )
    return requests.get('https://5sim.biz/v1/user/payments', headers=h, params=params).json()


def get_products(h=headers, country='russia', operator='any'):
    return requests.get('https://5sim.biz/v1/guest/products/' + country + '/' + operator, headers=h).json()


def get_prices_all(h=headers):
    return requests.get('https://5sim.biz/v1/guest/prices', headers=h).json()


def get_prices_by_country(h=headers, country='russia'):
    params = (
        ('country', country),
    )
    return requests.get('https://5sim.biz/v1/guest/prices', headers=h, params=params).json()


def get_prices_by_product(h=headers, product='google'):
    params = (
        ('product', product),
    )
    return requests.get('https://5sim.biz/v1/guest/prices', headers=h, params=params).json()[product]


def get_prices_by_country_and_product(h=headers, country='russia', product='google'):
    params = (
        ('country', country),
        ('product', product),
    )
    return requests.get('https://5sim.biz/v1/guest/prices', headers=h, params=params).json()


def buy_activation_number(h=headers, country='any', operator='any', product='google'):
    return requests.get('https://5sim.biz/v1/user/buy/activation/' + country + '/' + operator + '/' + product,
                        headers=h).json()


def buy_hosting_number(h=headers, country='any', operator='any', product='google'):
    return requests.get('https://5sim.biz/v1/user/buy/hosting/' + country + '/' + operator + '/' + product,
                        headers=h).json()


def buy_reuse_number(h=headers, product='amazon', number='79006665544'):
    return requests.get('https://5sim.biz/v1/user/reuse/' + product + '/' + number, headers=h).json()


def check_order(h=headers, id='1'):
    return requests.get('https://5sim.biz/v1/user/check/' + id, headers=h).json()


def finish_order(h=headers, id='1'):
    return requests.get('https://5sim.biz/v1/user/finish/' + id, headers=h).json()


def cancel_order(h=headers, id='1'):
    return requests.get('https://5sim.biz/v1/user/cancel/' + id, headers=h).json()


def ban_order(h=headers, id='1'):
    return requests.get('https://5sim.biz/v1/user/ban/' + id, headers=h).json()


def sms_list_order(h=headers, id='1'):
    return requests.get('https://5sim.biz/v1/user/sms/inbox/' + id, headers=h).json()


def get_notification(h=headers, lang='en'):
    return requests.get('https://5sim.biz/v1/guest/flash/' + lang, headers=h).json()


def get_county_list(h=headers):
    return requests.get('https://5sim.biz/v1/guest/countries', headers=h).json()


def get_number():
    req = get_prices_by_product()
    m = 100
    country = ''
    operator = ''
    # for i in req:
    for j in req['indonesia']:
        if m > req['indonesia'][j]['cost']:
            m = req['indonesia'][j]['cost']
            country = 'indonesia'
            operator = j
    return buy_activation_number(country=country, operator=operator, product='google')


if __name__ == 'main':
    pass
