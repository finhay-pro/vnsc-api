# Overview
There are 2 seperate sets of API to begin to trade with VNSC via API:
1. Obtain an trade token.
2. Using this token to place your own trade via [Trade API](trade.yaml)

# Obtaining token

This guide intends to support a quick way to start integrate with VNSC. This guide also assumes you have already opened an VNSC stock account, if not, download VNSC app and complete the eKYC process.

First, obtain a login token:
```
curl --location --request PUT 'https://api.vinasecurities.com/accounts/v1/login' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
    "username": "<phone_number>",
    "password": "<your_password>"
}'
```
Sample response:
```
{
    "error_code": "0",
    "message": "success",
    "result": {
        "user_id": 244,
        "access_token": "<access_token>",
        "refresh_token": "<refresh_token>",
        "cust_id": "0001000053",
        "required_change_password": false
    }
}
```

VNSC using JWT, and conform JWT standard. So for example, if you're using Postman, you also can use the `access_token` with Auth Type "Bearer Token" to try out the next request. Note the `user_id` field, it's used for sub-sequence requests.

Second, get list of sub-accounts. Each customer in VNSC will have 01 normal trading account and 01 margin trading account, this will help you get the id of accounts to use later with trading API.

```
curl --location 'https://api.vinasecurities.com/accounts/v1/users/244/sub-accounts' \
--header 'Authorization: Bearer <access_token>'
```
Sample response:
```
{
    "error_code": "0",
    "message": "success",
    "result": [
        {
            "id": "0001xxxxxx",
            "cust_id": "0001xxxxxx",
            "name": "Customer Full Name",
            "depository_number": "Custody Number",
            "product_type_name": ".1",
            "sub_account_ext": "120Cxxxxxx.1",
            "type": "Normal"
        },
        {
            "id": "0001xxxxxx",
            "cust_id": "0001xxxxxx",
            "name": "Customer Full Name",
            "depository_number": "Custody Number",
            "product_type_name": ".6",
            "sub_account_ext": "120Cxxxxxx.6",
            "type": "Margin"
        }
    ]
}
```

After this, you will need to acquire a trading token using login token, and it will be used independently with [Trade API](trade.yaml).

```
curl --location 'https://api.vinasecurities.com/auth/v2/otp' \
--header 'device-id: <id of your device>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "phone": "0916853668",
    "type": "TRADING_OTP"
}'
```
Sample response:
```
{
    "error_code": "0",
    "message": "success",
    "data": {
        "remain_second": 60,
        "message": "OTP đã được gửi",
        "otp_status": "SENT_OTP"
    }
}
```
After receiving your OTP via SMS, you can verify it and obtain the `trade_token` with your own `ttl` via:
```
curl --location 'https://api.vinasecurities.com/auth/v2/otp/verification' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access_token>' \
--data '{
    "phone": "0916853668",
    "type": "TRADING_OTP",
    "otp": "972873",
    "ttl": 604800 # 7 days
}'
```
Sample response:
```
{
    "error_code": "0",
    "message": "success",
    "result": {
        "token": "<trade_token>"
    }
}
```


# Trade
Please see [Trade API](trade.yaml). You can also use VNSC mobile app to verify that your order has indeed been placed into the system.