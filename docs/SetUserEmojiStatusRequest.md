# SetUserEmojiStatusRequest

Request parameters for setUserEmojiStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Unique identifier of the target user | 
**emoji_status_custom_emoji_id** | **str** | Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status. | [optional] 
**emoji_status_expiration_date** | **int** | Expiration date of the emoji status, if any | [optional] 

## Example

```python
from tele_rest.models.set_user_emoji_status_request import SetUserEmojiStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserEmojiStatusRequest from a JSON string
set_user_emoji_status_request_instance = SetUserEmojiStatusRequest.from_json(json)
# print the JSON string representation of the object
print(SetUserEmojiStatusRequest.to_json())

# convert the object into a dict
set_user_emoji_status_request_dict = set_user_emoji_status_request_instance.to_dict()
# create an instance of SetUserEmojiStatusRequest from a dict
set_user_emoji_status_request_from_dict = SetUserEmojiStatusRequest.from_dict(set_user_emoji_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


