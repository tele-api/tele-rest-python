# SetBusinessAccountGiftSettingsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**show_gift_button** | **bool** | Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field | 
**accepted_gift_types** | [**AcceptedGiftTypes**](AcceptedGiftTypes.md) |  | 

## Example

```python
from tele_rest.models.set_business_account_gift_settings_post_request import SetBusinessAccountGiftSettingsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountGiftSettingsPostRequest from a JSON string
set_business_account_gift_settings_post_request_instance = SetBusinessAccountGiftSettingsPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountGiftSettingsPostRequest.to_json())

# convert the object into a dict
set_business_account_gift_settings_post_request_dict = set_business_account_gift_settings_post_request_instance.to_dict()
# create an instance of SetBusinessAccountGiftSettingsPostRequest from a dict
set_business_account_gift_settings_post_request_from_dict = SetBusinessAccountGiftSettingsPostRequest.from_dict(set_business_account_gift_settings_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


