# SendDocumentPostRequestDocument

File to send. Pass a file\\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.send_document_post_request_document import SendDocumentPostRequestDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SendDocumentPostRequestDocument from a JSON string
send_document_post_request_document_instance = SendDocumentPostRequestDocument.from_json(json)
# print the JSON string representation of the object
print(SendDocumentPostRequestDocument.to_json())

# convert the object into a dict
send_document_post_request_document_dict = send_document_post_request_document_instance.to_dict()
# create an instance of SendDocumentPostRequestDocument from a dict
send_document_post_request_document_from_dict = SendDocumentPostRequestDocument.from_dict(send_document_post_request_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


