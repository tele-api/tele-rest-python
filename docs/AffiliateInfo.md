# AffiliateInfo

Contains information about the affiliate that received a commission via this transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_user** | [**User**](User.md) |  | [optional] 
**affiliate_chat** | [**Chat**](Chat.md) |  | [optional] 
**commission_per_mille** | **int** | The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users | 
**amount** | **int** | Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds | 
**nanostar_amount** | **int** | *Optional*. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds | [optional] 

## Example

```python
from tele_rest.models.affiliate_info import AffiliateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateInfo from a JSON string
affiliate_info_instance = AffiliateInfo.from_json(json)
# print the JSON string representation of the object
print(AffiliateInfo.to_json())

# convert the object into a dict
affiliate_info_dict = affiliate_info_instance.to_dict()
# create an instance of AffiliateInfo from a dict
affiliate_info_from_dict = AffiliateInfo.from_dict(affiliate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


