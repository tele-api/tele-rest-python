# PostGetGameHighScoresRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Target user id | 
**chat_id** | **int** | Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat | [optional] 
**message_id** | **int** | Required if *inline\\_message\\_id* is not specified. Identifier of the sent message | [optional] 
**inline_message_id** | **str** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 

## Example

```python
from tele_rest.models.post_get_game_high_scores_request import PostGetGameHighScoresRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetGameHighScoresRequest from a JSON string
post_get_game_high_scores_request_instance = PostGetGameHighScoresRequest.from_json(json)
# print the JSON string representation of the object
print(PostGetGameHighScoresRequest.to_json())

# convert the object into a dict
post_get_game_high_scores_request_dict = post_get_game_high_scores_request_instance.to_dict()
# create an instance of PostGetGameHighScoresRequest from a dict
post_get_game_high_scores_request_from_dict = PostGetGameHighScoresRequest.from_dict(post_get_game_high_scores_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


