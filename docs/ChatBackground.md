# ChatBackground

This object represents a chat background.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BackgroundType**](BackgroundType.md) |  | 

## Example

```python
from tele_rest.models.chat_background import ChatBackground

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBackground from a JSON string
chat_background_instance = ChatBackground.from_json(json)
# print the JSON string representation of the object
print(ChatBackground.to_json())

# convert the object into a dict
chat_background_dict = chat_background_instance.to_dict()
# create an instance of ChatBackground from a dict
chat_background_from_dict = ChatBackground.from_dict(chat_background_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


