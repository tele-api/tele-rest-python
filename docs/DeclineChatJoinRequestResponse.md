# DeclineChatJoinRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.decline_chat_join_request_response import DeclineChatJoinRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineChatJoinRequestResponse from a JSON string
decline_chat_join_request_response_instance = DeclineChatJoinRequestResponse.from_json(json)
# print the JSON string representation of the object
print(DeclineChatJoinRequestResponse.to_json())

# convert the object into a dict
decline_chat_join_request_response_dict = decline_chat_join_request_response_instance.to_dict()
# create an instance of DeclineChatJoinRequestResponse from a dict
decline_chat_join_request_response_from_dict = DeclineChatJoinRequestResponse.from_dict(decline_chat_join_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


