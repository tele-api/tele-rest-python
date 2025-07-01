# CopyTextButton

This object represents an inline keyboard button that copies specified text to the clipboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text to be copied to the clipboard; 1-256 characters | 

## Example

```python
from tele_rest.models.copy_text_button import CopyTextButton

# TODO update the JSON string below
json = "{}"
# create an instance of CopyTextButton from a JSON string
copy_text_button_instance = CopyTextButton.from_json(json)
# print the JSON string representation of the object
print(CopyTextButton.to_json())

# convert the object into a dict
copy_text_button_dict = copy_text_button_instance.to_dict()
# create an instance of CopyTextButton from a dict
copy_text_button_from_dict = CopyTextButton.from_dict(copy_text_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


