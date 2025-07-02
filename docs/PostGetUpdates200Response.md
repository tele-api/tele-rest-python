# PostGetUpdates200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[Update]**](Update.md) |  | 

## Example

```python
from tele_rest.models.post_get_updates200_response import PostGetUpdates200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUpdates200Response from a JSON string
post_get_updates200_response_instance = PostGetUpdates200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetUpdates200Response.to_json())

# convert the object into a dict
post_get_updates200_response_dict = post_get_updates200_response_instance.to_dict()
# create an instance of PostGetUpdates200Response from a dict
post_get_updates200_response_from_dict = PostGetUpdates200Response.from_dict(post_get_updates200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


