# GetChatRequestChatId

Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.get_chat_request_chat_id import GetChatRequestChatId

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatRequestChatId from a JSON string
get_chat_request_chat_id_instance = GetChatRequestChatId.from_json(json)
# print the JSON string representation of the object
print(GetChatRequestChatId.to_json())

# convert the object into a dict
get_chat_request_chat_id_dict = get_chat_request_chat_id_instance.to_dict()
# create an instance of GetChatRequestChatId from a dict
get_chat_request_chat_id_from_dict = GetChatRequestChatId.from_dict(get_chat_request_chat_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


