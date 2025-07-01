# SavePreparedInlineMessagePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user that can use the prepared message | 
**result** | [**InlineQueryResult**](InlineQueryResult.md) |  | 
**allow_user_chats** | **bool** | Pass *True* if the message can be sent to private chats with users | [optional] 
**allow_bot_chats** | **bool** | Pass *True* if the message can be sent to private chats with bots | [optional] 
**allow_group_chats** | **bool** | Pass *True* if the message can be sent to group and supergroup chats | [optional] 
**allow_channel_chats** | **bool** | Pass *True* if the message can be sent to channel chats | [optional] 

## Example

```python
from tele_rest.models.save_prepared_inline_message_post_request import SavePreparedInlineMessagePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SavePreparedInlineMessagePostRequest from a JSON string
save_prepared_inline_message_post_request_instance = SavePreparedInlineMessagePostRequest.from_json(json)
# print the JSON string representation of the object
print(SavePreparedInlineMessagePostRequest.to_json())

# convert the object into a dict
save_prepared_inline_message_post_request_dict = save_prepared_inline_message_post_request_instance.to_dict()
# create an instance of SavePreparedInlineMessagePostRequest from a dict
save_prepared_inline_message_post_request_from_dict = SavePreparedInlineMessagePostRequest.from_dict(save_prepared_inline_message_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


