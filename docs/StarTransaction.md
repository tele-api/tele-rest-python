# StarTransaction

Describes a Telegram Star transaction. Note that if the buyer initiates a chargeback with the payment provider from whom they acquired Stars (e.g., Apple, Google) following this transaction, the refunded Stars will be deducted from the bot's balance. This is outside of Telegram's control.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with *SuccessfulPayment.telegram\\_payment\\_charge\\_id* for successful incoming payments from users. | 
**amount** | **int** | Integer amount of Telegram Stars transferred by the transaction | 
**nanostar_amount** | **int** | *Optional*. The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999 | [optional] 
**var_date** | **int** | Date the transaction was created in Unix time | 
**source** | [**TransactionPartner**](TransactionPartner.md) |  | [optional] 
**receiver** | [**TransactionPartner**](TransactionPartner.md) |  | [optional] 

## Example

```python
from tele_rest.models.star_transaction import StarTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of StarTransaction from a JSON string
star_transaction_instance = StarTransaction.from_json(json)
# print the JSON string representation of the object
print(StarTransaction.to_json())

# convert the object into a dict
star_transaction_dict = star_transaction_instance.to_dict()
# create an instance of StarTransaction from a dict
star_transaction_from_dict = StarTransaction.from_dict(star_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


