# PostGetMyNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | A two-letter ISO 639-1 language code or an empty string | [optional] 

## Example

```python
from tele_rest.models.post_get_my_name_request import PostGetMyNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetMyNameRequest from a JSON string
post_get_my_name_request_instance = PostGetMyNameRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetMyNameRequest.to_json())

# convert the object into a dict
post_get_my_name_request_dict = post_get_my_name_request_instance.to_dict()
# create an instance of PostGetMyNameRequest from a dict
post_get_my_name_request_from_dict = PostGetMyNameRequest.from_dict(post_get_my_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


