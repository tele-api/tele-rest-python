# ForwardMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.forward_message_response import ForwardMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessageResponse from a JSON string
forward_message_response_instance = ForwardMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ForwardMessageResponse.to_json())

# convert the object into a dict
forward_message_response_dict = forward_message_response_instance.to_dict()
# create an instance of ForwardMessageResponse from a dict
forward_message_response_from_dict = ForwardMessageResponse.from_dict(forward_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


