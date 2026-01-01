# SendMessageDraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | **bool** |  | [default to True]

## Example

```python
from tele_rest.models.send_message_draft_response import SendMessageDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageDraftResponse from a JSON string
send_message_draft_response_instance = SendMessageDraftResponse.from_json(json)
# print the JSON string representation of the object
print(SendMessageDraftResponse.to_json())

# convert the object into a dict
send_message_draft_response_dict = send_message_draft_response_instance.to_dict()
# create an instance of SendMessageDraftResponse from a dict
send_message_draft_response_from_dict = SendMessageDraftResponse.from_dict(send_message_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


