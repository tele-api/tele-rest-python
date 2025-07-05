# SetBusinessAccountGiftSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_business_account_gift_settings_response import SetBusinessAccountGiftSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetBusinessAccountGiftSettingsResponse from a JSON string
set_business_account_gift_settings_response_instance = SetBusinessAccountGiftSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SetBusinessAccountGiftSettingsResponse.to_json())

# convert the object into a dict
set_business_account_gift_settings_response_dict = set_business_account_gift_settings_response_instance.to_dict()
# create an instance of SetBusinessAccountGiftSettingsResponse from a dict
set_business_account_gift_settings_response_from_dict = SetBusinessAccountGiftSettingsResponse.from_dict(set_business_account_gift_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


