# PostDeleteWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_pending_updates** | **bool** | Pass *True* to drop all pending updates | [optional] 

## Example

```python
from tele_rest.models.post_delete_webhook_request import PostDeleteWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteWebhookRequest from a JSON string
post_delete_webhook_request_instance = PostDeleteWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteWebhookRequest.to_json())

# convert the object into a dict
post_delete_webhook_request_dict = post_delete_webhook_request_instance.to_dict()
# create an instance of PostDeleteWebhookRequest from a dict
post_delete_webhook_request_from_dict = PostDeleteWebhookRequest.from_dict(post_delete_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


