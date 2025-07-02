# SendDiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_dice_response import SendDiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendDiceResponse from a JSON string
send_dice_response_instance = SendDiceResponse.from_json(json)
# print the JSON string representation of the object
print(SendDiceResponse.to_json())

# convert the object into a dict
send_dice_response_dict = send_dice_response_instance.to_dict()
# create an instance of SendDiceResponse from a dict
send_dice_response_from_dict = SendDiceResponse.from_dict(send_dice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


