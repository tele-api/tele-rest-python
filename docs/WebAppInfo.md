# WebAppInfo

Describes a [Web App](https://core.telegram.org/bots/webapps).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-mini-apps) | 

## Example

```python
from tele_rest.models.web_app_info import WebAppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebAppInfo from a JSON string
web_app_info_instance = WebAppInfo.from_json(json)
# print the JSON string representation of the object
print(WebAppInfo.to_json())

# convert the object into a dict
web_app_info_dict = web_app_info_instance.to_dict()
# create an instance of WebAppInfo from a dict
web_app_info_from_dict = WebAppInfo.from_dict(web_app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


