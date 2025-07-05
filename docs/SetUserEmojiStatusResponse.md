# SetUserEmojiStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_user_emoji_status_response import SetUserEmojiStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserEmojiStatusResponse from a JSON string
set_user_emoji_status_response_instance = SetUserEmojiStatusResponse.from_json(json)
# print the JSON string representation of the object
print(SetUserEmojiStatusResponse.to_json())

# convert the object into a dict
set_user_emoji_status_response_dict = set_user_emoji_status_response_instance.to_dict()
# create an instance of SetUserEmojiStatusResponse from a dict
set_user_emoji_status_response_from_dict = SetUserEmojiStatusResponse.from_dict(set_user_emoji_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


