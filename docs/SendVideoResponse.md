# SendVideoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_video_response import SendVideoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendVideoResponse from a JSON string
send_video_response_instance = SendVideoResponse.from_json(json)
# print the JSON string representation of the object
print(SendVideoResponse.to_json())

# convert the object into a dict
send_video_response_dict = send_video_response_instance.to_dict()
# create an instance of SendVideoResponse from a dict
send_video_response_from_dict = SendVideoResponse.from_dict(send_video_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


