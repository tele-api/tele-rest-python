# ChatJoinRequest

Represents a join request sent to a chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**Chat**](Chat.md) |  | 
**var_from** | [**User**](User.md) |  | 
**user_chat_id** | **int** | Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user. | 
**var_date** | **int** | Date the request was sent in Unix time | 
**bio** | **str** | *Optional*. Bio of the user. | [optional] 
**invite_link** | [**ChatInviteLink**](ChatInviteLink.md) |  | [optional] 

## Example

```python
from tele_rest.models.chat_join_request import ChatJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatJoinRequest from a JSON string
chat_join_request_instance = ChatJoinRequest.from_json(json)
# print the JSON string representation of the object
print(ChatJoinRequest.to_json())

# convert the object into a dict
chat_join_request_dict = chat_join_request_instance.to_dict()
# create an instance of ChatJoinRequest from a dict
chat_join_request_from_dict = ChatJoinRequest.from_dict(chat_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


