# ReactionTypeEmoji

The reaction is based on an emoji.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the reaction, always “emoji” | [default to 'emoji']
**emoji** | **str** | Reaction emoji. Currently, it can be one of \&quot;❤\&quot;, \&quot;👍\&quot;, \&quot;👎\&quot;, \&quot;🔥\&quot;, \&quot;🥰\&quot;, \&quot;👏\&quot;, \&quot;😁\&quot;, \&quot;🤔\&quot;, \&quot;🤯\&quot;, \&quot;😱\&quot;, \&quot;🤬\&quot;, \&quot;😢\&quot;, \&quot;🎉\&quot;, \&quot;🤩\&quot;, \&quot;🤮\&quot;, \&quot;💩\&quot;, \&quot;🙏\&quot;, \&quot;👌\&quot;, \&quot;🕊\&quot;, \&quot;🤡\&quot;, \&quot;🥱\&quot;, \&quot;🥴\&quot;, \&quot;😍\&quot;, \&quot;🐳\&quot;, \&quot;❤‍🔥\&quot;, \&quot;🌚\&quot;, \&quot;🌭\&quot;, \&quot;💯\&quot;, \&quot;🤣\&quot;, \&quot;⚡\&quot;, \&quot;🍌\&quot;, \&quot;🏆\&quot;, \&quot;💔\&quot;, \&quot;🤨\&quot;, \&quot;😐\&quot;, \&quot;🍓\&quot;, \&quot;🍾\&quot;, \&quot;💋\&quot;, \&quot;🖕\&quot;, \&quot;😈\&quot;, \&quot;😴\&quot;, \&quot;😭\&quot;, \&quot;🤓\&quot;, \&quot;👻\&quot;, \&quot;👨‍💻\&quot;, \&quot;👀\&quot;, \&quot;🎃\&quot;, \&quot;🙈\&quot;, \&quot;😇\&quot;, \&quot;😨\&quot;, \&quot;🤝\&quot;, \&quot;✍\&quot;, \&quot;🤗\&quot;, \&quot;🫡\&quot;, \&quot;🎅\&quot;, \&quot;🎄\&quot;, \&quot;☃\&quot;, \&quot;💅\&quot;, \&quot;🤪\&quot;, \&quot;🗿\&quot;, \&quot;🆒\&quot;, \&quot;💘\&quot;, \&quot;🙉\&quot;, \&quot;🦄\&quot;, \&quot;😘\&quot;, \&quot;💊\&quot;, \&quot;🙊\&quot;, \&quot;😎\&quot;, \&quot;👾\&quot;, \&quot;🤷‍♂\&quot;, \&quot;🤷\&quot;, \&quot;🤷‍♀\&quot;, \&quot;😡\&quot; | 

## Example

```python
from tele_rest.models.reaction_type_emoji import ReactionTypeEmoji

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionTypeEmoji from a JSON string
reaction_type_emoji_instance = ReactionTypeEmoji.from_json(json)
# print the JSON string representation of the object
print(ReactionTypeEmoji.to_json())

# convert the object into a dict
reaction_type_emoji_dict = reaction_type_emoji_instance.to_dict()
# create an instance of ReactionTypeEmoji from a dict
reaction_type_emoji_from_dict = ReactionTypeEmoji.from_dict(reaction_type_emoji_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


