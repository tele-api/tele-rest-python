# SendPaidMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_paid_media_response import SendPaidMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendPaidMediaResponse from a JSON string
send_paid_media_response_instance = SendPaidMediaResponse.from_json(json)
# print the JSON string representation of the object
print(SendPaidMediaResponse.to_json())

# convert the object into a dict
send_paid_media_response_dict = send_paid_media_response_instance.to_dict()
# create an instance of SendPaidMediaResponse from a dict
send_paid_media_response_from_dict = SendPaidMediaResponse.from_dict(send_paid_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


