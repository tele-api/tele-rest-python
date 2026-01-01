# GetChatGiftsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**OwnedGifts**](OwnedGifts.md) |  | 

## Example

```python
from tele_rest.models.get_chat_gifts_response import GetChatGiftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatGiftsResponse from a JSON string
get_chat_gifts_response_instance = GetChatGiftsResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatGiftsResponse.to_json())

# convert the object into a dict
get_chat_gifts_response_dict = get_chat_gifts_response_instance.to_dict()
# create an instance of GetChatGiftsResponse from a dict
get_chat_gifts_response_from_dict = GetChatGiftsResponse.from_dict(get_chat_gifts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


