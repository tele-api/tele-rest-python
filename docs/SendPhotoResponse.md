# SendPhotoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_photo_response import SendPhotoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendPhotoResponse from a JSON string
send_photo_response_instance = SendPhotoResponse.from_json(json)
# print the JSON string representation of the object
print(SendPhotoResponse.to_json())

# convert the object into a dict
send_photo_response_dict = send_photo_response_instance.to_dict()
# create an instance of SendPhotoResponse from a dict
send_photo_response_from_dict = SendPhotoResponse.from_dict(send_photo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


