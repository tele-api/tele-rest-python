# SetMyShortDescriptionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_description** | **str** | New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language. | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description. | [optional] 

## Example

```python
from tele_rest.models.set_my_short_description_post_request import SetMyShortDescriptionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMyShortDescriptionPostRequest from a JSON string
set_my_short_description_post_request_instance = SetMyShortDescriptionPostRequest.from_json(json)
# print the JSON string representation of the object
print(SetMyShortDescriptionPostRequest.to_json())

# convert the object into a dict
set_my_short_description_post_request_dict = set_my_short_description_post_request_instance.to_dict()
# create an instance of SetMyShortDescriptionPostRequest from a dict
set_my_short_description_post_request_from_dict = SetMyShortDescriptionPostRequest.from_dict(set_my_short_description_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


