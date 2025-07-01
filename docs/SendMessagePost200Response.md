# SendMessagePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_message_post200_response import SendMessagePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessagePost200Response from a JSON string
send_message_post200_response_instance = SendMessagePost200Response.from_json(json)
# print the JSON string representation of the object
print(SendMessagePost200Response.to_json())

# convert the object into a dict
send_message_post200_response_dict = send_message_post200_response_instance.to_dict()
# create an instance of SendMessagePost200Response from a dict
send_message_post200_response_from_dict = SendMessagePost200Response.from_dict(send_message_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


