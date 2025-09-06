# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-09-06T05:32:06.285336202Z[Etc/UTC]
- **Generator Version**: 7.14.0

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

from tele_rest.models.inline_query_result import InlineQueryResult

class TestInlineQueryResult(unittest.TestCase):
    """InlineQueryResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InlineQueryResult:
        """Test InlineQueryResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InlineQueryResult`
        """
        model = InlineQueryResult()
        if include_optional:
            return InlineQueryResult(
                type = 'voice',
                id = '',
                audio_file_id = '',
                caption = '',
                parse_mode = '',
                caption_entities = [
                    tele_rest.models.message_entity.MessageEntity(
                        type = 'mention', 
                        offset = 56, 
                        length = 56, 
                        url = '', 
                        user = tele_rest.models.user.User(
                            id = 56, 
                            is_bot = True, 
                            first_name = '', 
                            last_name = '', 
                            username = '', 
                            language_code = '', 
                            is_premium = True, 
                            added_to_attachment_menu = True, 
                            can_join_groups = True, 
                            can_read_all_group_messages = True, 
                            supports_inline_queries = True, 
                            can_connect_to_business = True, 
                            has_main_web_app = True, ), 
                        language = '', 
                        custom_emoji_id = '', )
                    ],
                reply_markup = tele_rest.models.inline_keyboard_markup.InlineKeyboardMarkup(
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
                        ], ),
                input_message_content = None,
                title = '',
                document_file_id = '',
                description = '',
                gif_file_id = '',
                show_caption_above_media = True,
                mpeg4_file_id = '',
                photo_file_id = '',
                sticker_file_id = '',
                video_file_id = '',
                voice_file_id = '',
                url = '',
                thumbnail_url = '',
                thumbnail_width = 56,
                thumbnail_height = 56,
                audio_url = '',
                performer = '',
                audio_duration = 56,
                phone_number = '',
                first_name = '',
                last_name = '',
                vcard = '',
                game_short_name = '',
                document_url = '',
                mime_type = 'text/html',
                gif_url = '',
                gif_width = 56,
                gif_height = 56,
                gif_duration = 56,
                thumbnail_mime_type = 'image/jpeg',
                latitude = 1.337,
                longitude = 1.337,
                horizontal_accuracy = 1.337,
                live_period = 56,
                heading = 56,
                proximity_alert_radius = 56,
                mpeg4_url = '',
                mpeg4_width = 56,
                mpeg4_height = 56,
                mpeg4_duration = 56,
                photo_url = '',
                photo_width = 56,
                photo_height = 56,
                address = '',
                foursquare_id = '',
                foursquare_type = '',
                google_place_id = '',
                google_place_type = '',
                video_url = '',
                video_width = 56,
                video_height = 56,
                video_duration = 56,
                voice_url = '',
                voice_duration = 56
            )
        else:
            return InlineQueryResult(
                type = 'voice',
                id = '',
                audio_file_id = '',
                input_message_content = None,
                title = '',
                document_file_id = '',
                gif_file_id = '',
                mpeg4_file_id = '',
                photo_file_id = '',
                sticker_file_id = '',
                video_file_id = '',
                voice_file_id = '',
                thumbnail_url = '',
                audio_url = '',
                phone_number = '',
                first_name = '',
                game_short_name = '',
                document_url = '',
                mime_type = 'text/html',
                gif_url = '',
                latitude = 1.337,
                longitude = 1.337,
                mpeg4_url = '',
                photo_url = '',
                address = '',
                video_url = '',
                voice_url = '',
        )
        """

    def testInlineQueryResult(self):
        """Test InlineQueryResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
