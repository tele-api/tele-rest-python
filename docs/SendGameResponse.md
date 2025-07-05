# SendGameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_game_response import SendGameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendGameResponse from a JSON string
send_game_response_instance = SendGameResponse.from_json(json)
# print the JSON string representation of the object
print(SendGameResponse.to_json())

# convert the object into a dict
send_game_response_dict = send_game_response_instance.to_dict()
# create an instance of SendGameResponse from a dict
send_game_response_from_dict = SendGameResponse.from_dict(send_game_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


