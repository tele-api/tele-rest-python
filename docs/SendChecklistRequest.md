# SendChecklistRequest

Request parameters for sendChecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | 
**chat_id** | **int** | Unique identifier for the target chat | 
**checklist** | [**InputChecklist**](InputChecklist.md) |  | 
**disable_notification** | **bool** | Sends the message silently. Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_checklist_request import SendChecklistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendChecklistRequest from a JSON string
send_checklist_request_instance = SendChecklistRequest.from_json(json)
# print the JSON string representation of the object
print(SendChecklistRequest.to_json())

# convert the object into a dict
send_checklist_request_dict = send_checklist_request_instance.to_dict()
# create an instance of SendChecklistRequest from a dict
send_checklist_request_from_dict = SendChecklistRequest.from_dict(send_checklist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


