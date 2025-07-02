# PostForwardMessages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[MessageId]**](MessageId.md) |  | 

## Example

```python
from tele_rest.models.post_forward_messages200_response import PostForwardMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostForwardMessages200Response from a JSON string
post_forward_messages200_response_instance = PostForwardMessages200Response.from_json(json)
# print the JSON string representation of the object
print(PostForwardMessages200Response.to_json())

# convert the object into a dict
post_forward_messages200_response_dict = post_forward_messages200_response_instance.to_dict()
# create an instance of PostForwardMessages200Response from a dict
post_forward_messages200_response_from_dict = PostForwardMessages200Response.from_dict(post_forward_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


