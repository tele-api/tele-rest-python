# SetBusinessAccountGiftSettingsRequest

Request parameters for setBusinessAccountGiftSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**show_gift_button** | **bool** | Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field | 
**accepted_gift_types** | [**AcceptedGiftTypes**](AcceptedGiftTypes.md) |  | 

## Example

```python
from tele_rest.models.set_business_account_gift_settings_request import SetBusinessAccountGiftSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountGiftSettingsRequest from a JSON string
set_business_account_gift_settings_request_instance = SetBusinessAccountGiftSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountGiftSettingsRequest.to_json())

# convert the object into a dict
set_business_account_gift_settings_request_dict = set_business_account_gift_settings_request_instance.to_dict()
# create an instance of SetBusinessAccountGiftSettingsRequest from a dict
set_business_account_gift_settings_request_from_dict = SetBusinessAccountGiftSettingsRequest.from_dict(set_business_account_gift_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


