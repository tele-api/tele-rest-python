# DeleteBusinessMessagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which to delete the messages | 
**message_ids** | **List[int]** | A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See [deleteMessage](https://core.telegram.org/bots/api/#deletemessage) for limitations on which messages can be deleted | 

## Example

```python
from tele_rest.models.delete_business_messages_post_request import DeleteBusinessMessagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBusinessMessagesPostRequest from a JSON string
delete_business_messages_post_request_instance = DeleteBusinessMessagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteBusinessMessagesPostRequest.to_json())

# convert the object into a dict
delete_business_messages_post_request_dict = delete_business_messages_post_request_instance.to_dict()
# create an instance of DeleteBusinessMessagesPostRequest from a dict
delete_business_messages_post_request_from_dict = DeleteBusinessMessagesPostRequest.from_dict(delete_business_messages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


