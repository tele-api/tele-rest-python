# SendDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**Message**](Message.md) |  | 

## Example

```python
from tele_rest.models.send_document_response import SendDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendDocumentResponse from a JSON string
send_document_response_instance = SendDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(SendDocumentResponse.to_json())

# convert the object into a dict
send_document_response_dict = send_document_response_instance.to_dict()
# create an instance of SendDocumentResponse from a dict
send_document_response_from_dict = SendDocumentResponse.from_dict(send_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


