# GetChatGiftsRequest

Request parameters for getChatGifts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**exclude_unsaved** | **bool** | Pass *True* to exclude gifts that aren&#39;t saved to the chat&#39;s profile page. Always *True*, unless the bot has the *can\\_post\\_messages* administrator right in the channel. | [optional] 
**exclude_saved** | **bool** | Pass *True* to exclude gifts that are saved to the chat&#39;s profile page. Always *False*, unless the bot has the *can\\_post\\_messages* administrator right in the channel. | [optional] 
**exclude_unlimited** | **bool** | Pass *True* to exclude gifts that can be purchased an unlimited number of times | [optional] 
**exclude_limited_upgradable** | **bool** | Pass *True* to exclude gifts that can be purchased a limited number of times and can be upgraded to unique | [optional] 
**exclude_limited_non_upgradable** | **bool** | Pass *True* to exclude gifts that can be purchased a limited number of times and can&#39;t be upgraded to unique | [optional] 
**exclude_from_blockchain** | **bool** | Pass *True* to exclude gifts that were assigned from the TON blockchain and can&#39;t be resold or transferred in Telegram | [optional] 
**exclude_unique** | **bool** | Pass *True* to exclude unique gifts | [optional] 
**sort_by_price** | **bool** | Pass *True* to sort results by gift price instead of send date. Sorting is applied before pagination. | [optional] 
**offset** | **str** | Offset of the first entry to return as received from the previous request; use an empty string to get the first chunk of results | [optional] 
**limit** | **int** | The maximum number of gifts to be returned; 1-100. Defaults to 100 | [optional] [default to 100]

## Example

```python
from tele_rest.models.get_chat_gifts_request import GetChatGiftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatGiftsRequest from a JSON string
get_chat_gifts_request_instance = GetChatGiftsRequest.from_json(json)
# print the JSON string representation of the object
print(GetChatGiftsRequest.to_json())

# convert the object into a dict
get_chat_gifts_request_dict = get_chat_gifts_request_instance.to_dict()
# create an instance of GetChatGiftsRequest from a dict
get_chat_gifts_request_from_dict = GetChatGiftsRequest.from_dict(get_chat_gifts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


