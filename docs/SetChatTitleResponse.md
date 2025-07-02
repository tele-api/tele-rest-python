# SetChatTitleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_chat_title_response import SetChatTitleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatTitleResponse from a JSON string
set_chat_title_response_instance = SetChatTitleResponse.from_json(json)
# print the JSON string representation of the object
print(SetChatTitleResponse.to_json())

# convert the object into a dict
set_chat_title_response_dict = set_chat_title_response_instance.to_dict()
# create an instance of SetChatTitleResponse from a dict
set_chat_title_response_from_dict = SetChatTitleResponse.from_dict(set_chat_title_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


