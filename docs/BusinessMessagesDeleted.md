# BusinessMessagesDeleted

This object is received when messages are deleted from a connected business account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**chat** | [**Chat**](Chat.md) |  | 
**message_ids** | **List[int]** | The list of identifiers of deleted messages in the chat of the business account | 

## Example

```python
from tele_rest.models.business_messages_deleted import BusinessMessagesDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessMessagesDeleted from a JSON string
business_messages_deleted_instance = BusinessMessagesDeleted.from_json(json)
# print the JSON string representation of the object
print(BusinessMessagesDeleted.to_json())

# convert the object into a dict
business_messages_deleted_dict = business_messages_deleted_instance.to_dict()
# create an instance of BusinessMessagesDeleted from a dict
business_messages_deleted_from_dict = BusinessMessagesDeleted.from_dict(business_messages_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


