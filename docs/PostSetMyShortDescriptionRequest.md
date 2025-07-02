# PostSetMyShortDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_description** | **str** | New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language. | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description. | [optional] 

## Example

```python
from tele_rest.models.post_set_my_short_description_request import PostSetMyShortDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMyShortDescriptionRequest from a JSON string
post_set_my_short_description_request_instance = PostSetMyShortDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMyShortDescriptionRequest.to_json())

# convert the object into a dict
post_set_my_short_description_request_dict = post_set_my_short_description_request_instance.to_dict()
# create an instance of PostSetMyShortDescriptionRequest from a dict
post_set_my_short_description_request_from_dict = PostSetMyShortDescriptionRequest.from_dict(post_set_my_short_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


