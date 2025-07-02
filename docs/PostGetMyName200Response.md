# PostGetMyName200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**BotName**](BotName.md) |  | 

## Example

```python
from tele_rest.models.post_get_my_name200_response import PostGetMyName200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetMyName200Response from a JSON string
post_get_my_name200_response_instance = PostGetMyName200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetMyName200Response.to_json())

# convert the object into a dict
post_get_my_name200_response_dict = post_get_my_name200_response_instance.to_dict()
# create an instance of PostGetMyName200Response from a dict
post_get_my_name200_response_from_dict = PostGetMyName200Response.from_dict(post_get_my_name200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


