# SendAnimationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_animation_response import SendAnimationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendAnimationResponse from a JSON string
send_animation_response_instance = SendAnimationResponse.from_json(json)
# print the JSON string representation of the object
print(SendAnimationResponse.to_json())

# convert the object into a dict
send_animation_response_dict = send_animation_response_instance.to_dict()
# create an instance of SendAnimationResponse from a dict
send_animation_response_from_dict = SendAnimationResponse.from_dict(send_animation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


