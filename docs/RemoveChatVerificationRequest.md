# RemoveChatVerificationRequest

Request parameters for removeChatVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 

## Example

```python
from tele_rest.models.remove_chat_verification_request import RemoveChatVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveChatVerificationRequest from a JSON string
remove_chat_verification_request_instance = RemoveChatVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveChatVerificationRequest.to_json())

# convert the object into a dict
remove_chat_verification_request_dict = remove_chat_verification_request_instance.to_dict()
# create an instance of RemoveChatVerificationRequest from a dict
remove_chat_verification_request_from_dict = RemoveChatVerificationRequest.from_dict(remove_chat_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


