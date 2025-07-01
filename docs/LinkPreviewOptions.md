# LinkPreviewOptions

Describes the options used for link preview generation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_disabled** | **bool** | *Optional*. *True*, if the link preview is disabled | [optional] 
**url** | **str** | *Optional*. URL to use for the link preview. If empty, then the first URL found in the message text will be used | [optional] 
**prefer_small_media** | **bool** | *Optional*. *True*, if the media in the link preview is supposed to be shrunk; ignored if the URL isn&#39;t explicitly specified or media size change isn&#39;t supported for the preview | [optional] 
**prefer_large_media** | **bool** | *Optional*. *True*, if the media in the link preview is supposed to be enlarged; ignored if the URL isn&#39;t explicitly specified or media size change isn&#39;t supported for the preview | [optional] 
**show_above_text** | **bool** | *Optional*. *True*, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text | [optional] 

## Example

```python
from tele_rest.models.link_preview_options import LinkPreviewOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LinkPreviewOptions from a JSON string
link_preview_options_instance = LinkPreviewOptions.from_json(json)
# print the JSON string representation of the object
print(LinkPreviewOptions.to_json())

# convert the object into a dict
link_preview_options_dict = link_preview_options_instance.to_dict()
# create an instance of LinkPreviewOptions from a dict
link_preview_options_from_dict = LinkPreviewOptions.from_dict(link_preview_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


