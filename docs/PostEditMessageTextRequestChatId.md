# PostEditMessageTextRequestChatId

Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_edit_message_text_request_chat_id import PostEditMessageTextRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditMessageTextRequestChatId from a JSON string
post_edit_message_text_request_chat_id_instance = PostEditMessageTextRequestChatId.from_json(json)
# print the JSON string representation of the object
print(PostEditMessageTextRequestChatId.to_json())

# convert the object into a dict
post_edit_message_text_request_chat_id_dict = post_edit_message_text_request_chat_id_instance.to_dict()
# create an instance of PostEditMessageTextRequestChatId from a dict
post_edit_message_text_request_chat_id_from_dict = PostEditMessageTextRequestChatId.from_dict(post_edit_message_text_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


