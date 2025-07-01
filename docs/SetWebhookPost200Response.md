# SetWebhookPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.set_webhook_post200_response import SetWebhookPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetWebhookPost200Response from a JSON string
set_webhook_post200_response_instance = SetWebhookPost200Response.from_json(json)
# print the JSON string representation of the object
print(SetWebhookPost200Response.to_json())

# convert the object into a dict
set_webhook_post200_response_dict = set_webhook_post200_response_instance.to_dict()
# create an instance of SetWebhookPost200Response from a dict
set_webhook_post200_response_from_dict = SetWebhookPost200Response.from_dict(set_webhook_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


