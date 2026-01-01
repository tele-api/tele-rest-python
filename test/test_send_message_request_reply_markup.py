# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2026 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.3.0
- **Modified**: 2026-01-01T02:06:09.762570119Z[Etc/UTC]
- **Generator Version**: 7.18.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Telegram Bot API service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501

import unittest

from tele_rest.models.send_message_request_reply_markup import SendMessageRequestReplyMarkup

class TestSendMessageRequestReplyMarkup(unittest.TestCase):
    """SendMessageRequestReplyMarkup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendMessageRequestReplyMarkup:
        """Test SendMessageRequestReplyMarkup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendMessageRequestReplyMarkup`
        """
        model = SendMessageRequestReplyMarkup()
        if include_optional:
            return SendMessageRequestReplyMarkup(
                inline_keyboard = [
                    [
                        tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                            text = '', 
                            url = '', 
                            callback_data = '', 
                            web_app = tele_rest.models.web_app_info.WebAppInfo(
                                url = '', ), 
                            login_url = tele_rest.models.login_url.LoginUrl(
                                url = '', 
                                forward_text = '', 
                                bot_username = '', 
                                request_write_access = True, ), 
                            switch_inline_query = '', 
                            switch_inline_query_current_chat = '', 
                            switch_inline_query_chosen_chat = tele_rest.models.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat(
                                query = '', 
                                allow_user_chats = True, 
                                allow_bot_chats = True, 
                                allow_group_chats = True, 
                                allow_channel_chats = True, ), 
                            copy_text = tele_rest.models.copy_text_button.CopyTextButton(
                                text = '0', ), 
                            callback_game = null, 
                            pay = True, )
                        ]
                    ],
                keyboard = [
                    [
                        tele_rest.models.keyboard_button.KeyboardButton(
                            text = '', 
                            request_users = tele_rest.models.keyboard_button_request_users.KeyboardButtonRequestUsers(
                                request_id = 56, 
                                user_is_bot = True, 
                                user_is_premium = True, 
                                max_quantity = 56, 
                                request_name = True, 
                                request_username = True, 
                                request_photo = True, ), 
                            request_chat = tele_rest.models.keyboard_button_request_chat.KeyboardButtonRequestChat(
                                request_id = 56, 
                                chat_is_channel = True, 
                                chat_is_forum = True, 
                                chat_has_username = True, 
                                chat_is_created = True, 
                                user_administrator_rights = tele_rest.models.chat_administrator_rights.ChatAdministratorRights(
                                    is_anonymous = True, 
                                    can_manage_chat = True, 
                                    can_delete_messages = True, 
                                    can_manage_video_chats = True, 
                                    can_restrict_members = True, 
                                    can_promote_members = True, 
                                    can_change_info = True, 
                                    can_invite_users = True, 
                                    can_post_stories = True, 
                                    can_edit_stories = True, 
                                    can_delete_stories = True, 
                                    can_post_messages = True, 
                                    can_edit_messages = True, 
                                    can_pin_messages = True, 
                                    can_manage_topics = True, 
                                    can_manage_direct_messages = True, ), 
                                bot_administrator_rights = tele_rest.models.chat_administrator_rights.ChatAdministratorRights(
                                    is_anonymous = True, 
                                    can_manage_chat = True, 
                                    can_delete_messages = True, 
                                    can_manage_video_chats = True, 
                                    can_restrict_members = True, 
                                    can_promote_members = True, 
                                    can_change_info = True, 
                                    can_invite_users = True, 
                                    can_post_stories = True, 
                                    can_edit_stories = True, 
                                    can_delete_stories = True, 
                                    can_post_messages = True, 
                                    can_edit_messages = True, 
                                    can_pin_messages = True, 
                                    can_manage_topics = True, 
                                    can_manage_direct_messages = True, ), 
                                bot_is_member = True, 
                                request_title = True, 
                                request_username = True, 
                                request_photo = True, ), 
                            request_contact = True, 
                            request_location = True, 
                            request_poll = tele_rest.models.keyboard_button_poll_type.KeyboardButtonPollType(
                                type = '', ), 
                            web_app = tele_rest.models.web_app_info.WebAppInfo(
                                url = '', ), )
                        ]
                    ],
                is_persistent = True,
                resize_keyboard = True,
                one_time_keyboard = True,
                input_field_placeholder = '0',
                selective = True,
                remove_keyboard = True,
                force_reply = True
            )
        else:
            return SendMessageRequestReplyMarkup(
                inline_keyboard = [
                    [
                        tele_rest.models.inline_keyboard_button.InlineKeyboardButton(
                            text = '', 
                            url = '', 
                            callback_data = '', 
                            web_app = tele_rest.models.web_app_info.WebAppInfo(
                                url = '', ), 
                            login_url = tele_rest.models.login_url.LoginUrl(
                                url = '', 
                                forward_text = '', 
                                bot_username = '', 
                                request_write_access = True, ), 
                            switch_inline_query = '', 
                            switch_inline_query_current_chat = '', 
                            switch_inline_query_chosen_chat = tele_rest.models.switch_inline_query_chosen_chat.SwitchInlineQueryChosenChat(
                                query = '', 
                                allow_user_chats = True, 
                                allow_bot_chats = True, 
                                allow_group_chats = True, 
                                allow_channel_chats = True, ), 
                            copy_text = tele_rest.models.copy_text_button.CopyTextButton(
                                text = '0', ), 
                            callback_game = null, 
                            pay = True, )
                        ]
                    ],
                keyboard = [
                    [
                        tele_rest.models.keyboard_button.KeyboardButton(
                            text = '', 
                            request_users = tele_rest.models.keyboard_button_request_users.KeyboardButtonRequestUsers(
                                request_id = 56, 
                                user_is_bot = True, 
                                user_is_premium = True, 
                                max_quantity = 56, 
                                request_name = True, 
                                request_username = True, 
                                request_photo = True, ), 
                            request_chat = tele_rest.models.keyboard_button_request_chat.KeyboardButtonRequestChat(
                                request_id = 56, 
                                chat_is_channel = True, 
                                chat_is_forum = True, 
                                chat_has_username = True, 
                                chat_is_created = True, 
                                user_administrator_rights = tele_rest.models.chat_administrator_rights.ChatAdministratorRights(
                                    is_anonymous = True, 
                                    can_manage_chat = True, 
                                    can_delete_messages = True, 
                                    can_manage_video_chats = True, 
                                    can_restrict_members = True, 
                                    can_promote_members = True, 
                                    can_change_info = True, 
                                    can_invite_users = True, 
                                    can_post_stories = True, 
                                    can_edit_stories = True, 
                                    can_delete_stories = True, 
                                    can_post_messages = True, 
                                    can_edit_messages = True, 
                                    can_pin_messages = True, 
                                    can_manage_topics = True, 
                                    can_manage_direct_messages = True, ), 
                                bot_administrator_rights = tele_rest.models.chat_administrator_rights.ChatAdministratorRights(
                                    is_anonymous = True, 
                                    can_manage_chat = True, 
                                    can_delete_messages = True, 
                                    can_manage_video_chats = True, 
                                    can_restrict_members = True, 
                                    can_promote_members = True, 
                                    can_change_info = True, 
                                    can_invite_users = True, 
                                    can_post_stories = True, 
                                    can_edit_stories = True, 
                                    can_delete_stories = True, 
                                    can_post_messages = True, 
                                    can_edit_messages = True, 
                                    can_pin_messages = True, 
                                    can_manage_topics = True, 
                                    can_manage_direct_messages = True, ), 
                                bot_is_member = True, 
                                request_title = True, 
                                request_username = True, 
                                request_photo = True, ), 
                            request_contact = True, 
                            request_location = True, 
                            request_poll = tele_rest.models.keyboard_button_poll_type.KeyboardButtonPollType(
                                type = '', ), 
                            web_app = tele_rest.models.web_app_info.WebAppInfo(
                                url = '', ), )
                        ]
                    ],
                remove_keyboard = True,
                force_reply = True,
        )
        """

    def testSendMessageRequestReplyMarkup(self):
        """Test SendMessageRequestReplyMarkup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
