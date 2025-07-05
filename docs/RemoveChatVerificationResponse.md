# RemoveChatVerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.remove_chat_verification_response import RemoveChatVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveChatVerificationResponse from a JSON string
remove_chat_verification_response_instance = RemoveChatVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveChatVerificationResponse.to_json())

# convert the object into a dict
remove_chat_verification_response_dict = remove_chat_verification_response_instance.to_dict()
# create an instance of RemoveChatVerificationResponse from a dict
remove_chat_verification_response_from_dict = RemoveChatVerificationResponse.from_dict(remove_chat_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


