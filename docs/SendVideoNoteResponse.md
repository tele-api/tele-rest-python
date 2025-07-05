# SendVideoNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_video_note_response import SendVideoNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendVideoNoteResponse from a JSON string
send_video_note_response_instance = SendVideoNoteResponse.from_json(json)
# print the JSON string representation of the object
print(SendVideoNoteResponse.to_json())

# convert the object into a dict
send_video_note_response_dict = send_video_note_response_instance.to_dict()
# create an instance of SendVideoNoteResponse from a dict
send_video_note_response_from_dict = SendVideoNoteResponse.from_dict(send_video_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


