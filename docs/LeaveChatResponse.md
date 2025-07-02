# LeaveChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.leave_chat_response import LeaveChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveChatResponse from a JSON string
leave_chat_response_instance = LeaveChatResponse.from_json(json)
# print the JSON string representation of the object
print(LeaveChatResponse.to_json())

# convert the object into a dict
leave_chat_response_dict = leave_chat_response_instance.to_dict()
# create an instance of LeaveChatResponse from a dict
leave_chat_response_from_dict = LeaveChatResponse.from_dict(leave_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


