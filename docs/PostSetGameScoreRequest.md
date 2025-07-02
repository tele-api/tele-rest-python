# PostSetGameScoreRequest


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
from tele_rest.models.post_set_game_score_request import PostSetGameScoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSetGameScoreRequest from a JSON string
post_set_game_score_request_instance = PostSetGameScoreRequest.from_json(json)
# print the JSON string representation of the object
print(PostSetGameScoreRequest.to_json())

# convert the object into a dict
post_set_game_score_request_dict = post_set_game_score_request_instance.to_dict()
# create an instance of PostSetGameScoreRequest from a dict
post_set_game_score_request_from_dict = PostSetGameScoreRequest.from_dict(post_set_game_score_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


