# SetChatTitlePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessagePostRequestChatId**](SendMessagePostRequestChatId.md) |  | 
**title** | **str** | New chat title, 1-128 characters | 

## Example

```python
from tele_rest.models.set_chat_title_post_request import SetChatTitlePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetChatTitlePostRequest from a JSON string
set_chat_title_post_request_instance = SetChatTitlePostRequest.from_json(json)
# print the JSON string representation of the object
print(SetChatTitlePostRequest.to_json())

# convert the object into a dict
set_chat_title_post_request_dict = set_chat_title_post_request_instance.to_dict()
# create an instance of SetChatTitlePostRequest from a dict
set_chat_title_post_request_from_dict = SetChatTitlePostRequest.from_dict(set_chat_title_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


