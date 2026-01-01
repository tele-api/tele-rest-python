# RepostStoryRequest

Request parameters for repostStory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection | 
**from_chat_id** | **int** | Unique identifier of the chat which posted the story that should be reposted | 
**from_story_id** | **int** | Unique identifier of the story that should be reposted | 
**active_period** | **int** | Period after which the story is moved to the archive, in seconds; must be one of &#x60;6 * 3600&#x60;, &#x60;12 * 3600&#x60;, &#x60;86400&#x60;, or &#x60;2 * 86400&#x60; | 
**post_to_chat_page** | **bool** | Pass *True* to keep the story accessible after it expires | [optional] 
**protect_content** | **bool** | Pass *True* if the content of the story must be protected from forwarding and screenshotting | [optional] 

## Example

```python
from tele_rest.models.repost_story_request import RepostStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepostStoryRequest from a JSON string
repost_story_request_instance = RepostStoryRequest.from_json(json)
# print the JSON string representation of the object
print(RepostStoryRequest.to_json())

# convert the object into a dict
repost_story_request_dict = repost_story_request_instance.to_dict()
# create an instance of RepostStoryRequest from a dict
repost_story_request_from_dict = RepostStoryRequest.from_dict(repost_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


