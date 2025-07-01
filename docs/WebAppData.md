# WebAppData

Describes data sent from a [Web App](https://core.telegram.org/bots/webapps) to the bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The data. Be aware that a bad client can send arbitrary data in this field. | 
**button_text** | **str** | Text of the *web\\_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field. | 

## Example

```python
from tele_rest.models.web_app_data import WebAppData

# TODO update the JSON string below
json = "{}"
# create an instance of WebAppData from a JSON string
web_app_data_instance = WebAppData.from_json(json)
# print the JSON string representation of the object
print(WebAppData.to_json())

# convert the object into a dict
web_app_data_dict = web_app_data_instance.to_dict()
# create an instance of WebAppData from a dict
web_app_data_from_dict = WebAppData.from_dict(web_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


