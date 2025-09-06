# VerifyChatRequest

Request parameters for verifyChat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**VerifyChatRequestChatId**](VerifyChatRequestChatId.md) |  | 
**custom_description** | **str** | Custom description for the verification; 0-70 characters. Must be empty if the organization isn&#39;t allowed to provide a custom verification description. | [optional] 

## Example

```python
from tele_rest.models.verify_chat_request import VerifyChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyChatRequest from a JSON string
verify_chat_request_instance = VerifyChatRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyChatRequest.to_json())

# convert the object into a dict
verify_chat_request_dict = verify_chat_request_instance.to_dict()
# create an instance of VerifyChatRequest from a dict
verify_chat_request_from_dict = VerifyChatRequest.from_dict(verify_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


