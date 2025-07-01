# EditMessageTextPostRequestChatId

Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.edit_message_text_post_request_chat_id import EditMessageTextPostRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageTextPostRequestChatId from a JSON string
edit_message_text_post_request_chat_id_instance = EditMessageTextPostRequestChatId.from_json(json)
# print the JSON string representation of the object
print(EditMessageTextPostRequestChatId.to_json())

# convert the object into a dict
edit_message_text_post_request_chat_id_dict = edit_message_text_post_request_chat_id_instance.to_dict()
# create an instance of EditMessageTextPostRequestChatId from a dict
edit_message_text_post_request_chat_id_from_dict = EditMessageTextPostRequestChatId.from_dict(edit_message_text_post_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


