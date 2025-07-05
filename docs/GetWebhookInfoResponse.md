# GetWebhookInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**WebhookInfo**](WebhookInfo.md) |  | 

## Example

```python
from tele_rest.models.get_webhook_info_response import GetWebhookInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookInfoResponse from a JSON string
get_webhook_info_response_instance = GetWebhookInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebhookInfoResponse.to_json())

# convert the object into a dict
get_webhook_info_response_dict = get_webhook_info_response_instance.to_dict()
# create an instance of GetWebhookInfoResponse from a dict
get_webhook_info_response_from_dict = GetWebhookInfoResponse.from_dict(get_webhook_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


