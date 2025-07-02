# DeleteBusinessMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.delete_business_messages_response import DeleteBusinessMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBusinessMessagesResponse from a JSON string
delete_business_messages_response_instance = DeleteBusinessMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteBusinessMessagesResponse.to_json())

# convert the object into a dict
delete_business_messages_response_dict = delete_business_messages_response_instance.to_dict()
# create an instance of DeleteBusinessMessagesResponse from a dict
delete_business_messages_response_from_dict = DeleteBusinessMessagesResponse.from_dict(delete_business_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


