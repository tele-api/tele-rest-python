# Poll

This object contains information about a poll.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique poll identifier | 
**question** | **str** | Poll question, 1-300 characters | 
**question_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities that appear in the *question*. Currently, only custom emoji entities are allowed in poll questions | [optional] 
**options** | [**List[PollOption]**](PollOption.md) | List of poll options | 
**total_voter_count** | **int** | Total number of users that voted in the poll | 
**is_closed** | **bool** | *True*, if the poll is closed | 
**is_anonymous** | **bool** | *True*, if the poll is anonymous | 
**type** | **str** | Poll type, currently can be “regular” or “quiz” | 
**allows_multiple_answers** | **bool** | *True*, if the poll allows multiple answers | 
**correct_option_id** | **int** | *Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot. | [optional] 
**explanation** | **str** | *Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters | [optional] 
**explanation_entities** | [**List[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation* | [optional] 
**open_period** | **int** | *Optional*. Amount of time in seconds the poll will be active after creation | [optional] 
**close_date** | **int** | *Optional*. Point in time (Unix timestamp) when the poll will be automatically closed | [optional] 

## Example

```python
from tele_rest.models.poll import Poll

# TODO update the JSON string below
json = "{}"
# create an instance of Poll from a JSON string
poll_instance = Poll.from_json(json)
# print the JSON string representation of the object
print(Poll.to_json())

# convert the object into a dict
poll_dict = poll_instance.to_dict()
# create an instance of Poll from a dict
poll_from_dict = Poll.from_dict(poll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


