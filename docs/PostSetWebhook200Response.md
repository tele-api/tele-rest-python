# PostSetWebhook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.post_set_webhook200_response import PostSetWebhook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetWebhook200Response from a JSON string
post_set_webhook200_response_instance = PostSetWebhook200Response.from_json(json)
# print the JSON string representation of the object
print(PostSetWebhook200Response.to_json())

# convert the object into a dict
post_set_webhook200_response_dict = post_set_webhook200_response_instance.to_dict()
# create an instance of PostSetWebhook200Response from a dict
post_set_webhook200_response_from_dict = PostSetWebhook200Response.from_dict(post_set_webhook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


