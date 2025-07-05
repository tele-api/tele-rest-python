# EditMessageTextRequestChatId

Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.edit_message_text_request_chat_id import EditMessageTextRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of EditMessageTextRequestChatId from a JSON string
edit_message_text_request_chat_id_instance = EditMessageTextRequestChatId.from_json(json)
# print the JSON string representation of the object
print(EditMessageTextRequestChatId.to_json())

# convert the object into a dict
edit_message_text_request_chat_id_dict = edit_message_text_request_chat_id_instance.to_dict()
# create an instance of EditMessageTextRequestChatId from a dict
edit_message_text_request_chat_id_from_dict = EditMessageTextRequestChatId.from_dict(edit_message_text_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


