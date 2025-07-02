# ApproveChatJoinRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.approve_chat_join_request_response import ApproveChatJoinRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveChatJoinRequestResponse from a JSON string
approve_chat_join_request_response_instance = ApproveChatJoinRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ApproveChatJoinRequestResponse.to_json())

# convert the object into a dict
approve_chat_join_request_response_dict = approve_chat_join_request_response_instance.to_dict()
# create an instance of ApproveChatJoinRequestResponse from a dict
approve_chat_join_request_response_from_dict = ApproveChatJoinRequestResponse.from_dict(approve_chat_join_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


