# Update

This [object](https://core.telegram.org/bots/api/#available-types) represents an incoming update.   At most **one** of the optional parameters can be present in any given update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_id** | **int** | The update&#39;s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you&#39;re using [webhooks](https://core.telegram.org/bots/api/#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially. | 
**message** | [**Message**](Message.md) |  | [optional] 
**edited_message** | [**Message**](Message.md) |  | [optional] 
**channel_post** | [**Message**](Message.md) |  | [optional] 
**edited_channel_post** | [**Message**](Message.md) |  | [optional] 
**business_connection** | [**BusinessConnection**](BusinessConnection.md) |  | [optional] 
**business_message** | [**Message**](Message.md) |  | [optional] 
**edited_business_message** | [**Message**](Message.md) |  | [optional] 
**deleted_business_messages** | [**BusinessMessagesDeleted**](BusinessMessagesDeleted.md) |  | [optional] 
**message_reaction** | [**MessageReactionUpdated**](MessageReactionUpdated.md) |  | [optional] 
**message_reaction_count** | [**MessageReactionCountUpdated**](MessageReactionCountUpdated.md) |  | [optional] 
**inline_query** | [**InlineQuery**](InlineQuery.md) |  | [optional] 
**chosen_inline_result** | [**ChosenInlineResult**](ChosenInlineResult.md) |  | [optional] 
**callback_query** | [**CallbackQuery**](CallbackQuery.md) |  | [optional] 
**shipping_query** | [**ShippingQuery**](ShippingQuery.md) |  | [optional] 
**pre_checkout_query** | [**PreCheckoutQuery**](PreCheckoutQuery.md) |  | [optional] 
**purchased_paid_media** | [**PaidMediaPurchased**](PaidMediaPurchased.md) |  | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**poll_answer** | [**PollAnswer**](PollAnswer.md) |  | [optional] 
**my_chat_member** | [**ChatMemberUpdated**](ChatMemberUpdated.md) |  | [optional] 
**chat_member** | [**ChatMemberUpdated**](ChatMemberUpdated.md) |  | [optional] 
**chat_join_request** | [**ChatJoinRequest**](ChatJoinRequest.md) |  | [optional] 
**chat_boost** | [**ChatBoostUpdated**](ChatBoostUpdated.md) |  | [optional] 
**removed_chat_boost** | [**ChatBoostRemoved**](ChatBoostRemoved.md) |  | [optional] 

## Example

```python
from tele_rest.models.update import Update

# TODO update the JSON string below
json = "{}"
# create an instance of Update from a JSON string
update_instance = Update.from_json(json)
# print the JSON string representation of the object
print(Update.to_json())

# convert the object into a dict
update_dict = update_instance.to_dict()
# create an instance of Update from a dict
update_from_dict = Update.from_dict(update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


