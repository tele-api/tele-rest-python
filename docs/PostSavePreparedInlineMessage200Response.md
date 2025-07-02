# PostSavePreparedInlineMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**PreparedInlineMessage**](PreparedInlineMessage.md) |  | 

## Example

```python
from tele_rest.models.post_save_prepared_inline_message200_response import PostSavePreparedInlineMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavePreparedInlineMessage200Response from a JSON string
post_save_prepared_inline_message200_response_instance = PostSavePreparedInlineMessage200Response.from_json(json)
# print the JSON string representation of the object
print(PostSavePreparedInlineMessage200Response.to_json())

# convert the object into a dict
post_save_prepared_inline_message200_response_dict = post_save_prepared_inline_message200_response_instance.to_dict()
# create an instance of PostSavePreparedInlineMessage200Response from a dict
post_save_prepared_inline_message200_response_from_dict = PostSavePreparedInlineMessage200Response.from_dict(post_save_prepared_inline_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


