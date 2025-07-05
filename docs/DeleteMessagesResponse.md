# DeleteMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_messages_response import DeleteMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMessagesResponse from a JSON string
delete_messages_response_instance = DeleteMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteMessagesResponse.to_json())

# convert the object into a dict
delete_messages_response_dict = delete_messages_response_instance.to_dict()
# create an instance of DeleteMessagesResponse from a dict
delete_messages_response_from_dict = DeleteMessagesResponse.from_dict(delete_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


