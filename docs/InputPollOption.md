# InputPollOption

This object contains information about one answer option in a poll to be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Option text, 1-100 characters | 
**text_parse_mode** | **str** | *Optional*. Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Currently, only custom emoji entities are allowed | [optional] 
**text_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text\\_parse\\_mode* | [optional] 

## Example

```python
from tele_rest.models.input_poll_option import InputPollOption

# TODO update the JSON string below
json = "{}"
# create an instance of InputPollOption from a JSON string
input_poll_option_instance = InputPollOption.from_json(json)
# print the JSON string representation of the object
print(InputPollOption.to_json())

# convert the object into a dict
input_poll_option_dict = input_poll_option_instance.to_dict()
# create an instance of InputPollOption from a dict
input_poll_option_from_dict = InputPollOption.from_dict(input_poll_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


