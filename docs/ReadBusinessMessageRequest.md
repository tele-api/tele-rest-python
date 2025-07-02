# ReadBusinessMessageRequest

Request parameters for readBusinessMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which to read the message | 
**chat_id** | **int** | Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours. | 
**message_id** | **int** | Unique identifier of the message to mark as read | 

## Example

```python
from tele_rest.models.read_business_message_request import ReadBusinessMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReadBusinessMessageRequest from a JSON string
read_business_message_request_instance = ReadBusinessMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ReadBusinessMessageRequest.to_json())

# convert the object into a dict
read_business_message_request_dict = read_business_message_request_instance.to_dict()
# create an instance of ReadBusinessMessageRequest from a dict
read_business_message_request_from_dict = ReadBusinessMessageRequest.from_dict(read_business_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


