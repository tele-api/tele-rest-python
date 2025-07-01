# SendGiftPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Required if *chat\\_id* is not specified. Unique identifier of the target user who will receive the gift. | [optional] 
**chat_id** | [**SendGiftPostRequestChatId**](SendGiftPostRequestChatId.md) |  | [optional] 
**gift_id** | **str** | Identifier of the gift | 
**pay_for_upgrade** | **bool** | Pass *True* to pay for the gift upgrade from the bot&#39;s balance, thereby making the upgrade free for the receiver | [optional] 
**text** | **str** | Text that will be shown along with the gift; 0-128 characters | [optional] 
**text_parse_mode** | **str** | Mode for parsing entities in the text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored. | [optional] 
**text_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text\\_parse\\_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom\\_emoji” are ignored. | [optional] 

## Example

```python
from tele_rest.models.send_gift_post_request import SendGiftPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendGiftPostRequest from a JSON string
send_gift_post_request_instance = SendGiftPostRequest.from_json(json)
# print the JSON string representation of the object
print(SendGiftPostRequest.to_json())

# convert the object into a dict
send_gift_post_request_dict = send_gift_post_request_instance.to_dict()
# create an instance of SendGiftPostRequest from a dict
send_gift_post_request_from_dict = SendGiftPostRequest.from_dict(send_gift_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


