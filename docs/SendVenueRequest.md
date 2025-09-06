# SendVenueRequest

Request parameters for sendVenue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_connection_id** | **str** | Unique identifier of the business connection on behalf of which the message will be sent | [optional] 
**chat_id** | [**SendMessageRequestChatId**](SendMessageRequestChatId.md) |  | 
**message_thread_id** | **int** | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only | [optional] 
**direct_messages_topic_id** | **int** | Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat | [optional] 
**latitude** | **float** | Latitude of the venue | 
**longitude** | **float** | Longitude of the venue | 
**title** | **str** | Name of the venue | 
**address** | **str** | Address of the venue | 
**foursquare_id** | **str** | Foursquare identifier of the venue | [optional] 
**foursquare_type** | **str** | Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.) | [optional] 
**google_place_id** | **str** | Google Places identifier of the venue | [optional] 
**google_place_type** | **str** | Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) | [optional] 
**disable_notification** | **bool** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**protect_content** | **bool** | Protects the contents of the sent message from forwarding and saving | [optional] 
**allow_paid_broadcast** | **bool** | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot&#39;s balance | [optional] 
**message_effect_id** | **str** | Unique identifier of the message effect to be added to the message; for private chats only | [optional] 
**suggested_post_parameters** | [**SuggestedPostParameters**](SuggestedPostParameters.md) |  | [optional] 
**reply_parameters** | [**ReplyParameters**](ReplyParameters.md) |  | [optional] 
**reply_markup** | [**SendMessageRequestReplyMarkup**](SendMessageRequestReplyMarkup.md) |  | [optional] 

## Example

```python
from tele_rest.models.send_venue_request import SendVenueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendVenueRequest from a JSON string
send_venue_request_instance = SendVenueRequest.from_json(json)
# print the JSON string representation of the object
print(SendVenueRequest.to_json())

# convert the object into a dict
send_venue_request_dict = send_venue_request_instance.to_dict()
# create an instance of SendVenueRequest from a dict
send_venue_request_from_dict = SendVenueRequest.from_dict(send_venue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


