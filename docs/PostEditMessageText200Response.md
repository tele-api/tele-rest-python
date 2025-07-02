# PostEditMessageText200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**PostEditMessageText200ResponseResult**](PostEditMessageText200ResponseResult.md) |  | 

## Example

```python
from tele_rest.models.post_edit_message_text200_response import PostEditMessageText200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditMessageText200Response from a JSON string
post_edit_message_text200_response_instance = PostEditMessageText200Response.from_json(json)
# print the JSON string representation of the object
print(PostEditMessageText200Response.to_json())

# convert the object into a dict
post_edit_message_text200_response_dict = post_edit_message_text200_response_instance.to_dict()
# create an instance of PostEditMessageText200Response from a dict
post_edit_message_text200_response_from_dict = PostEditMessageText200Response.from_dict(post_edit_message_text200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


