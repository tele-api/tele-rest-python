# TransactionPartnerChat

Describes a transaction with a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the transaction partner, always “chat” | [default to 'chat']
**chat** | [**Chat**](Chat.md) |  | 
**gift** | [**Gift**](Gift.md) |  | [optional] 

## Example

```python
from tele_rest.models.transaction_partner_chat import TransactionPartnerChat

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPartnerChat from a JSON string
transaction_partner_chat_instance = TransactionPartnerChat.from_json(json)
# print the JSON string representation of the object
print(TransactionPartnerChat.to_json())

# convert the object into a dict
transaction_partner_chat_dict = transaction_partner_chat_instance.to_dict()
# create an instance of TransactionPartnerChat from a dict
transaction_partner_chat_from_dict = TransactionPartnerChat.from_dict(transaction_partner_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


