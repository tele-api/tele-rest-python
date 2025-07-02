# GetGameHighScoresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [default to True]
**result** | [**List[GameHighScore]**](GameHighScore.md) |  | 

## Example

```python
from tele_rest.models.get_game_high_scores_response import GetGameHighScoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameHighScoresResponse from a JSON string
get_game_high_scores_response_instance = GetGameHighScoresResponse.from_json(json)
# print the JSON string representation of the object
print(GetGameHighScoresResponse.to_json())

# convert the object into a dict
get_game_high_scores_response_dict = get_game_high_scores_response_instance.to_dict()
# create an instance of GetGameHighScoresResponse from a dict
get_game_high_scores_response_from_dict = GetGameHighScoresResponse.from_dict(get_game_high_scores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


