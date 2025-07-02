# PostSetMyDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language. | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description. | [optional] 

## Example

```python
from tele_rest.models.post_set_my_description_request import PostSetMyDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMyDescriptionRequest from a JSON string
post_set_my_description_request_instance = PostSetMyDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMyDescriptionRequest.to_json())

# convert the object into a dict
post_set_my_description_request_dict = post_set_my_description_request_instance.to_dict()
# create an instance of PostSetMyDescriptionRequest from a dict
post_set_my_description_request_from_dict = PostSetMyDescriptionRequest.from_dict(post_set_my_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


