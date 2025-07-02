# SendMediaGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Message]**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_media_group_response import SendMediaGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendMediaGroupResponse from a JSON string
send_media_group_response_instance = SendMediaGroupResponse.from_json(json)
# print the JSON string representation of the object
print(SendMediaGroupResponse.to_json())

# convert the object into a dict
send_media_group_response_dict = send_media_group_response_instance.to_dict()
# create an instance of SendMediaGroupResponse from a dict
send_media_group_response_from_dict = SendMediaGroupResponse.from_dict(send_media_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


