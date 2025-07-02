# BusinessBotRights

Represents the rights of a business bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_reply** | **bool** | *Optional*. True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours | [optional] [default to True]
**can_read_messages** | **bool** | *Optional*. True, if the bot can mark incoming private messages as read | [optional] [default to True]
**can_delete_outgoing_messages** | **bool** | *Optional*. True, if the bot can delete messages sent by the bot | [optional] [default to True]
**can_delete_all_messages** | **bool** | *Optional*. True, if the bot can delete all private messages in managed chats | [optional] [default to True]
**can_edit_name** | **bool** | *Optional*. True, if the bot can edit the first and last name of the business account | [optional] [default to True]
**can_edit_bio** | **bool** | *Optional*. True, if the bot can edit the bio of the business account | [optional] [default to True]
**can_edit_profile_photo** | **bool** | *Optional*. True, if the bot can edit the profile photo of the business account | [optional] [default to True]
**can_edit_username** | **bool** | *Optional*. True, if the bot can edit the username of the business account | [optional] [default to True]
**can_change_gift_settings** | **bool** | *Optional*. True, if the bot can change the privacy settings pertaining to gifts for the business account | [optional] [default to True]
**can_view_gifts_and_stars** | **bool** | *Optional*. True, if the bot can view gifts and the amount of Telegram Stars owned by the business account | [optional] [default to True]
**can_convert_gifts_to_stars** | **bool** | *Optional*. True, if the bot can convert regular gifts owned by the business account to Telegram Stars | [optional] [default to True]
**can_transfer_and_upgrade_gifts** | **bool** | *Optional*. True, if the bot can transfer and upgrade gifts owned by the business account | [optional] [default to True]
**can_transfer_stars** | **bool** | *Optional*. True, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts | [optional] [default to True]
**can_manage_stories** | **bool** | *Optional*. True, if the bot can post, edit and delete stories on behalf of the business account | [optional] [default to True]

## Example

```python
from tele_rest.models.business_bot_rights import BusinessBotRights

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessBotRights from a JSON string
business_bot_rights_instance = BusinessBotRights.from_json(json)
# print the JSON string representation of the object
print(BusinessBotRights.to_json())

# convert the object into a dict
business_bot_rights_dict = business_bot_rights_instance.to_dict()
# create an instance of BusinessBotRights from a dict
business_bot_rights_from_dict = BusinessBotRights.from_dict(business_bot_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


