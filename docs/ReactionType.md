# ReactionType

This object describes the type of a reaction. Currently, it can be one of  * [ReactionTypeEmoji](https://core.telegram.org/bots/api/#reactiontypeemoji) * [ReactionTypeCustomEmoji](https://core.telegram.org/bots/api/#reactiontypecustomemoji) * [ReactionTypePaid](https://core.telegram.org/bots/api/#reactiontypepaid)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the reaction, always “paid” | [default to 'paid']
**emoji** | **str** | Reaction emoji. Currently, it can be one of \&quot;❤\&quot;, \&quot;👍\&quot;, \&quot;👎\&quot;, \&quot;🔥\&quot;, \&quot;🥰\&quot;, \&quot;👏\&quot;, \&quot;😁\&quot;, \&quot;🤔\&quot;, \&quot;🤯\&quot;, \&quot;😱\&quot;, \&quot;🤬\&quot;, \&quot;😢\&quot;, \&quot;🎉\&quot;, \&quot;🤩\&quot;, \&quot;🤮\&quot;, \&quot;💩\&quot;, \&quot;🙏\&quot;, \&quot;👌\&quot;, \&quot;🕊\&quot;, \&quot;🤡\&quot;, \&quot;🥱\&quot;, \&quot;🥴\&quot;, \&quot;😍\&quot;, \&quot;🐳\&quot;, \&quot;❤‍🔥\&quot;, \&quot;🌚\&quot;, \&quot;🌭\&quot;, \&quot;💯\&quot;, \&quot;🤣\&quot;, \&quot;⚡\&quot;, \&quot;🍌\&quot;, \&quot;🏆\&quot;, \&quot;💔\&quot;, \&quot;🤨\&quot;, \&quot;😐\&quot;, \&quot;🍓\&quot;, \&quot;🍾\&quot;, \&quot;💋\&quot;, \&quot;🖕\&quot;, \&quot;😈\&quot;, \&quot;😴\&quot;, \&quot;😭\&quot;, \&quot;🤓\&quot;, \&quot;👻\&quot;, \&quot;👨‍💻\&quot;, \&quot;👀\&quot;, \&quot;🎃\&quot;, \&quot;🙈\&quot;, \&quot;😇\&quot;, \&quot;😨\&quot;, \&quot;🤝\&quot;, \&quot;✍\&quot;, \&quot;🤗\&quot;, \&quot;🫡\&quot;, \&quot;🎅\&quot;, \&quot;🎄\&quot;, \&quot;☃\&quot;, \&quot;💅\&quot;, \&quot;🤪\&quot;, \&quot;🗿\&quot;, \&quot;🆒\&quot;, \&quot;💘\&quot;, \&quot;🙉\&quot;, \&quot;🦄\&quot;, \&quot;😘\&quot;, \&quot;💊\&quot;, \&quot;🙊\&quot;, \&quot;😎\&quot;, \&quot;👾\&quot;, \&quot;🤷‍♂\&quot;, \&quot;🤷\&quot;, \&quot;🤷‍♀\&quot;, \&quot;😡\&quot; | 
**custom_emoji_id** | **str** | Custom emoji identifier | 

## Example

```python
from tele_rest.models.reaction_type import ReactionType

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionType from a JSON string
reaction_type_instance = ReactionType.from_json(json)
# print the JSON string representation of the object
print(ReactionType.to_json())

# convert the object into a dict
reaction_type_dict = reaction_type_instance.to_dict()
# create an instance of ReactionType from a dict
reaction_type_from_dict = ReactionType.from_dict(reaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


