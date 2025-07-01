# ReplyParameters

Describes reply parameters for the message that is being sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int** | Identifier of the message that will be replied to in the current chat, or in the chat *chat\\_id* if it is specified | 
**chat_id** | [**ReplyParametersChatId**](ReplyParametersChatId.md) |  | [optional] 
**allow_sending_without_reply** | **bool** | *Optional*. Pass *True* if the message should be sent even if the specified message to be replied to is not found. Always *False* for replies in another chat or forum topic. Always *True* for messages sent on behalf of a business account. | [optional] 
**quote** | **str** | *Optional*. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom\\_emoji* entities. The message will fail to send if the quote isn&#39;t found in the original message. | [optional] 
**quote_parse_mode** | **str** | *Optional*. Mode for parsing entities in the quote. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**quote_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of *quote\\_parse\\_mode*. | [optional] 
**quote_position** | **int** | *Optional*. Position of the quote in the original message in UTF-16 code units | [optional] 

## Example

```python
from tele_rest.models.reply_parameters import ReplyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyParameters from a JSON string
reply_parameters_instance = ReplyParameters.from_json(json)
# print the JSON string representation of the object
print(ReplyParameters.to_json())

# convert the object into a dict
reply_parameters_dict = reply_parameters_instance.to_dict()
# create an instance of ReplyParameters from a dict
reply_parameters_from_dict = ReplyParameters.from_dict(reply_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


