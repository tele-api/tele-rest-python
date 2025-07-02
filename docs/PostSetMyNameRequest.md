# PostSetMyNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language. | [optional] 
**language_code** | **str** | A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name. | [optional] 

## Example

```python
from tele_rest.models.post_set_my_name_request import PostSetMyNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetMyNameRequest from a JSON string
post_set_my_name_request_instance = PostSetMyNameRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetMyNameRequest.to_json())

# convert the object into a dict
post_set_my_name_request_dict = post_set_my_name_request_instance.to_dict()
# create an instance of PostSetMyNameRequest from a dict
post_set_my_name_request_from_dict = PostSetMyNameRequest.from_dict(post_set_my_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


