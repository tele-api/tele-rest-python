# PostGetGameHighScores200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[GameHighScore]**](GameHighScore.md) |  | 

## Example

```python
from tele_rest.models.post_get_game_high_scores200_response import PostGetGameHighScores200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetGameHighScores200Response from a JSON string
post_get_game_high_scores200_response_instance = PostGetGameHighScores200Response.from_json(json)
# print the JSON string representation of the object
print(PostGetGameHighScores200Response.to_json())

# convert the object into a dict
post_get_game_high_scores200_response_dict = post_get_game_high_scores200_response_instance.to_dict()
# create an instance of PostGetGameHighScores200Response from a dict
post_get_game_high_scores200_response_from_dict = PostGetGameHighScores200Response.from_dict(post_get_game_high_scores200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


