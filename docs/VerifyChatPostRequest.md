# VerifyChatPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**custom_description** | **str** | Custom description for the verification; 0-70 characters. Must be empty if the organization isn&#39;t allowed to provide a custom verification description. | [optional] 

## Example

```python
from tele_rest.models.verify_chat_post_request import VerifyChatPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyChatPostRequest from a JSON string
verify_chat_post_request_instance = VerifyChatPostRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyChatPostRequest.to_json())

# convert the object into a dict
verify_chat_post_request_dict = verify_chat_post_request_instance.to_dict()
# create an instance of VerifyChatPostRequest from a dict
verify_chat_post_request_from_dict = VerifyChatPostRequest.from_dict(verify_chat_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


