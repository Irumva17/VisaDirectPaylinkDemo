import requests
import json
from data import user_id, password, cert, key

url_push = "https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


payload = json.loads(
    """
    {
        "surcharge": "11.99",
        "amount": 124.02,
        "localTransactionDateTime": "2023-05-05T12:00:00",
        "cpsAuthorizationCharacteristicsIndicator": "Y",
        "riskAssessmentData": {
            "traExemptionIndicator": "true",
            "trustedMerchantExemptionIndicator": "true",
            "scpExemptionIndicator": "true",
            "delegatedAuthenticationIndicator": "true",
            "lowValueExemptionIndicator": "true"
        },
        "colombiaNationalServiceData": {
            "addValueTaxReturn": 10,
            "taxAmountConsumption": 10,
            "nationalNetReimbursementFeeBaseAmount": 20,
            "addValueTaxAmount": 10,
            "nationalNetMiscAmount": 10,
            "countryCodeNationalService": 170,
            "nationalChargebackReason": 11,
            "emvTransactionIndicator": "1",
            "nationalNetMiscAmountType": "A",
            "costTransactionIndicator": "0",
            "nationalReimbursementFee": 20
        },
        "cardAcceptor": {
            "address": {
            "country": "USA",
            "zipCode": "94404",
            "county": "081",
            "state": "CA"
            },
            "idCode": "ABCD1234ABCD123",
            "name": "Visa Inc. USA-Foster City",
            "terminalId": "ABCD1234"
        },
        "acquirerCountryCode": 840,
        "acquiringBin": 408999,
        "senderCurrencyCode": "USD",
        "retrievalReferenceNumber": "330000560021",
        "addressVerificationData": {
            "street": "XYZ St",
            "postalCode": "12345"
        },
        "cavv": "0700100038238906000013405823891061668252",
        "systemsTraceAuditNumber": 452011,
        "businessApplicationId": "AA",
        "senderPrimaryAccountNumber": "4060320000000127",
        "settlementServiceIndicator": 9,
        "visaMerchantIdentifier": "73625198",
        "foreignExchangeFeeTransaction": 11.99,
        "senderCardExpiryDate": "2023-10",
        "nationalReimbursementFee": 11.22
    }

    """
    )

timeout = 30


# 1. Push Funds Transaction
try:
    response = requests.post(
        url_push,
        cert=(cert, key),
        # verify=ca_cert,
        auth=(user_id, password),
        headers=headers,
        json=payload,
        timeout=timeout
    )

    print("PushFunds - Status Code:", response.status_code)
    print("PushFunds - Response Body:", response.text)

    data = response.json()
    transaction_id = data.get("transactionIdentifier")

except Exception as e:
    print("Error during PushFunds:", str(e))
    transaction_id = None

# Query Transaction 

if transaction_id:
    url_query = f"https://sandbox.api.visa.com/visadirect/fundstransfer/v1/transactionquery"

    query_payload = {
        "acquiringBin": "408999",
        "transactionIdentifier": transaction_id
    }

    try:
        response_query = requests.post(
            url_query,
            cert=(cert, key),
            # verify=ca_cert,
            auth=(user_id, password),
            headers=headers,
            json=query_payload,
            timeout=timeout
        )

        print("Query - Status Code:", response_query.status_code)
        print("Query - Response Body:", response_query.text)

    except Exception as e:
        print("Error during Query:", str(e))
