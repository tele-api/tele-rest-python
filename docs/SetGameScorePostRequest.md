# SetGameScorePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User identifier | 
**score** | **int** | New score, must be non-negative | 
**force** | **bool** | Pass *True* if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters | [optional] 
**disable_edit_message** | **bool** | Pass *True* if the game message should not be automatically edited to include the current scoreboard | [optional] 
**chat_id** | **int** | Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the sent message | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 

## Example

```python
from tele_rest.models.set_game_score_post_request import SetGameScorePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetGameScorePostRequest from a JSON string
set_game_score_post_request_instance = SetGameScorePostRequest.from_json(json)
# print the JSON string representation of the object
print(SetGameScorePostRequest.to_json())

# convert the object into a dict
set_game_score_post_request_dict = set_game_score_post_request_instance.to_dict()
# create an instance of SetGameScorePostRequest from a dict
set_game_score_post_request_from_dict = SetGameScorePostRequest.from_dict(set_game_score_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


