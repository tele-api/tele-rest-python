# SetWebhookRequest

Request parameters for setWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS URL to send updates to. Use an empty string to remove webhook integration | 
**certificate** | **object** |  | [optional] 
**ip_address** | **str** | The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS | [optional] 
**max_connections** | **int** | The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot&#39;s server, and higher values to increase your bot&#39;s throughput. | [optional] [default to 40]
**allowed_updates** | **List[str]** | A JSON-serialized list of the update types you want your bot to receive. For example, specify &#x60;[\&quot;message\&quot;, \&quot;edited_channel_post\&quot;, \&quot;callback_query\&quot;]&#x60; to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all update types except *chat\\_member*, *message\\_reaction*, and *message\\_reaction\\_count* (default). If not specified, the previous setting will be used.   Please note that this parameter doesn&#39;t affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time. | [optional] 
**drop_pending_updates** | **bool** | Pass *True* to drop all pending updates | [optional] 
**secret_token** | **str** | A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters &#x60;A-Z&#x60;, &#x60;a-z&#x60;, &#x60;0-9&#x60;, &#x60;_&#x60; and &#x60;-&#x60; are allowed. The header is useful to ensure that the request comes from a webhook set by you. | [optional] 

## Example

```python
from tele_rest.models.set_webhook_request import SetWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetWebhookRequest from a JSON string
set_webhook_request_instance = SetWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(SetWebhookRequest.to_json())

# convert the object into a dict
set_webhook_request_dict = set_webhook_request_instance.to_dict()
# create an instance of SetWebhookRequest from a dict
set_webhook_request_from_dict = SetWebhookRequest.from_dict(set_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


