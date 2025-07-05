# DeleteWebhookRequest

Request parameters for deleteWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_pending_updates** | **bool** | Pass *True* to drop all pending updates | [optional] 

## Example

```python
from tele_rest.models.delete_webhook_request import DeleteWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhookRequest from a JSON string
delete_webhook_request_instance = DeleteWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWebhookRequest.to_json())

# convert the object into a dict
delete_webhook_request_dict = delete_webhook_request_instance.to_dict()
# create an instance of DeleteWebhookRequest from a dict
delete_webhook_request_from_dict = DeleteWebhookRequest.from_dict(delete_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


