# ForwardMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[MessageId]**](MessageId.md) |  | 

## Example

```python
from tele_rest.models.forward_messages_response import ForwardMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessagesResponse from a JSON string
forward_messages_response_instance = ForwardMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(ForwardMessagesResponse.to_json())

# convert the object into a dict
forward_messages_response_dict = forward_messages_response_instance.to_dict()
# create an instance of ForwardMessagesResponse from a dict
forward_messages_response_from_dict = ForwardMessagesResponse.from_dict(forward_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


