# TextQuote

This object contains information about the quoted part of a message that is replied to by the given message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text of the quoted part of a message that is replied to by the given message | 
**entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the quote. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, and *custom\\_emoji* entities are kept in quotes. | [optional] 
**position** | **int** | Approximate quote position in the original message in UTF-16 code units as specified by the sender | 
**is_manual** | **bool** | *Optional*. *True*, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server. | [optional] [default to True]

## Example

```python
from tele_rest.models.text_quote import TextQuote

# TODO update the JSON string below
json = "{}"
# create an instance of TextQuote from a JSON string
text_quote_instance = TextQuote.from_json(json)
# print the JSON string representation of the object
print(TextQuote.to_json())

# convert the object into a dict
text_quote_dict = text_quote_instance.to_dict()
# create an instance of TextQuote from a dict
text_quote_from_dict = TextQuote.from_dict(text_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


