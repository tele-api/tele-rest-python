# GiftPremiumSubscriptionRequest

Request parameters for giftPremiumSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user who will receive a Telegram Premium subscription | 
**month_count** | **int** | Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12 | 
**star_count** | **int** | Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months | 
**text** | **str** | Text that will be shown along with the service message about the subscription; 0-128 characters | [optional] 
**text_parse_mode** | **str** | Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored. | [optional] 
**text_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text\\_parse\\_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored. | [optional] 

## Example

```python
from tele_rest.models.gift_premium_subscription_request import GiftPremiumSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GiftPremiumSubscriptionRequest from a JSON string
gift_premium_subscription_request_instance = GiftPremiumSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(GiftPremiumSubscriptionRequest.to_json())

# convert the object into a dict
gift_premium_subscription_request_dict = gift_premium_subscription_request_instance.to_dict()
# create an instance of GiftPremiumSubscriptionRequest from a dict
gift_premium_subscription_request_from_dict = GiftPremiumSubscriptionRequest.from_dict(gift_premium_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


