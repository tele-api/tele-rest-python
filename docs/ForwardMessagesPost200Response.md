# ForwardMessagesPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[MessageId]**](MessageId.md) |  | 

## Example

```python
from tele_rest.models.forward_messages_post200_response import ForwardMessagesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardMessagesPost200Response from a JSON string
forward_messages_post200_response_instance = ForwardMessagesPost200Response.from_json(json)
# print the JSON string representation of the object
print(ForwardMessagesPost200Response.to_json())

# convert the object into a dict
forward_messages_post200_response_dict = forward_messages_post200_response_instance.to_dict()
# create an instance of ForwardMessagesPost200Response from a dict
forward_messages_post200_response_from_dict = ForwardMessagesPost200Response.from_dict(forward_messages_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


