# BackgroundTypeChatTheme

The background is taken directly from a built-in chat theme.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the background, always “chat\\_theme” | [default to 'chat_theme']
**theme_name** | **str** | Name of the chat theme, which is usually an emoji | 

## Example

```python
from tele_rest.models.background_type_chat_theme import BackgroundTypeChatTheme

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundTypeChatTheme from a JSON string
background_type_chat_theme_instance = BackgroundTypeChatTheme.from_json(json)
# print the JSON string representation of the object
print(BackgroundTypeChatTheme.to_json())

# convert the object into a dict
background_type_chat_theme_dict = background_type_chat_theme_instance.to_dict()
# create an instance of BackgroundTypeChatTheme from a dict
background_type_chat_theme_from_dict = BackgroundTypeChatTheme.from_dict(background_type_chat_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


