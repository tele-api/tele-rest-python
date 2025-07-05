# PostStoryRequest

Request parameters for postStory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**content** | [**InputStoryContent**](InputStoryContent.md) |  | 
**active_period** | **int** | Period after which the story is moved to the archive, in seconds; must be one of &#x60;6 * 3600&#x60;, &#x60;12 * 3600&#x60;, &#x60;86400&#x60;, or &#x60;2 * 86400&#x60; | 
**caption** | **str** | Caption of the story, 0-2048 characters after entities parsing | [optional] 
**parse_mode** | **str** | Mode for parsing entities in the story caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**caption_entities** | [**List[MessageEntity]**](MessageEntity.md) | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**areas** | [**List[StoryArea]**](StoryArea.md) | A JSON-serialized list of clickable areas to be shown on the story | [optional] 
**post_to_chat_page** | **bool** | Pass *True* to keep the story accessible after it expires | [optional] 
**protect_content** | **bool** | Pass *True* if the content of the story must be protected from forwarding and screenshotting | [optional] 

## Example

```python
from tele_rest.models.post_story_request import PostStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStoryRequest from a JSON string
post_story_request_instance = PostStoryRequest.from_json(json)
# print the JSON string representation of the object
print(PostStoryRequest.to_json())

# convert the object into a dict
post_story_request_dict = post_story_request_instance.to_dict()
# create an instance of PostStoryRequest from a dict
post_story_request_from_dict = PostStoryRequest.from_dict(post_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


