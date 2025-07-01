# WriteAccessAllowed

This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_request** | **bool** | *Optional*. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps) | [optional] 
**web_app_name** | **str** | *Optional*. Name of the Web App, if the access was granted when the Web App was launched from a link | [optional] 
**from_attachment_menu** | **bool** | *Optional*. True, if the access was granted when the bot was added to the attachment or side menu | [optional] 

## Example

```python
from tele_rest.models.write_access_allowed import WriteAccessAllowed

# TODO update the JSON string below
json = "{}"
# create an instance of WriteAccessAllowed from a JSON string
write_access_allowed_instance = WriteAccessAllowed.from_json(json)
# print the JSON string representation of the object
print(WriteAccessAllowed.to_json())

# convert the object into a dict
write_access_allowed_dict = write_access_allowed_instance.to_dict()
# create an instance of WriteAccessAllowed from a dict
write_access_allowed_from_dict = WriteAccessAllowed.from_dict(write_access_allowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


