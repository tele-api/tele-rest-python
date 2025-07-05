# SendContactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_contact_response import SendContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendContactResponse from a JSON string
send_contact_response_instance = SendContactResponse.from_json(json)
# print the JSON string representation of the object
print(SendContactResponse.to_json())

# convert the object into a dict
send_contact_response_dict = send_contact_response_instance.to_dict()
# create an instance of SendContactResponse from a dict
send_contact_response_from_dict = SendContactResponse.from_dict(send_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


