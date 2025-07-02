# PostSendDocumentRequestDocument

File to send. Pass a file\\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](https://core.telegram.org/bots/api/#sending-files)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tele_rest.models.post_send_document_request_document import PostSendDocumentRequestDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PostSendDocumentRequestDocument from a JSON string
post_send_document_request_document_instance = PostSendDocumentRequestDocument.from_json(json)
# print the JSON string representation of the object
print(PostSendDocumentRequestDocument.to_json())

# convert the object into a dict
post_send_document_request_document_dict = post_send_document_request_document_instance.to_dict()
# create an instance of PostSendDocumentRequestDocument from a dict
post_send_document_request_document_from_dict = PostSendDocumentRequestDocument.from_dict(post_send_document_request_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


