# SendGiftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.send_gift_response import SendGiftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendGiftResponse from a JSON string
send_gift_response_instance = SendGiftResponse.from_json(json)
# print the JSON string representation of the object
print(SendGiftResponse.to_json())

# convert the object into a dict
send_gift_response_dict = send_gift_response_instance.to_dict()
# create an instance of SendGiftResponse from a dict
send_gift_response_from_dict = SendGiftResponse.from_dict(send_gift_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


