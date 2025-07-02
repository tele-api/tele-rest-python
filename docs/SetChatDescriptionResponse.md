# SetChatDescriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_chat_description_response import SetChatDescriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatDescriptionResponse from a JSON string
set_chat_description_response_instance = SetChatDescriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SetChatDescriptionResponse.to_json())

# convert the object into a dict
set_chat_description_response_dict = set_chat_description_response_instance.to_dict()
# create an instance of SetChatDescriptionResponse from a dict
set_chat_description_response_from_dict = SetChatDescriptionResponse.from_dict(set_chat_description_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


