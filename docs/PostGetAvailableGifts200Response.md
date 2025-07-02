# PostGetAvailableGifts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Gifts**](Gifts.md) |  | 

## Example

```python
from tele_rest.models.post_get_available_gifts200_response import PostGetAvailableGifts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetAvailableGifts200Response from a JSON string
post_get_available_gifts200_response_instance = PostGetAvailableGifts200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetAvailableGifts200Response.to_json())

# convert the object into a dict
post_get_available_gifts200_response_dict = post_get_available_gifts200_response_instance.to_dict()
# create an instance of PostGetAvailableGifts200Response from a dict
post_get_available_gifts200_response_from_dict = PostGetAvailableGifts200Response.from_dict(post_get_available_gifts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


