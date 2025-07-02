# PostReadBusinessMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which to read the message | 
**chat_id** | **int** | Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours. | 
**message_id** | **int** | Unique identifier of the message to mark as read | 

## Example

```python
from tele_rest.models.post_read_business_message_request import PostReadBusinessMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReadBusinessMessageRequest from a JSON string
post_read_business_message_request_instance = PostReadBusinessMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PostReadBusinessMessageRequest.to_json())

# convert the object into a dict
post_read_business_message_request_dict = post_read_business_message_request_instance.to_dict()
# create an instance of PostReadBusinessMessageRequest from a dict
post_read_business_message_request_from_dict = PostReadBusinessMessageRequest.from_dict(post_read_business_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


