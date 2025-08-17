# coding: utf-8

"""
Telegram Bot API - REST API Client
The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram. To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 9.2.0
- **Modified**: 2025-08-17T02:10:52.303427632Z[Etc/UTC]
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

from tele_rest.models.owned_gift import OwnedGift

class TestOwnedGift(unittest.TestCase):
    """OwnedGift unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OwnedGift:
        """Test OwnedGift
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OwnedGift`
        """
        model = OwnedGift()
        if include_optional:
            return OwnedGift(
                type = 'unique',
                gift = tele_rest.models.unique_gift.UniqueGift(
                    base_name = '', 
                    name = '', 
                    number = 56, 
                    model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                        name = '', 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            thumbnail = tele_rest.models.photo_size.PhotoSize(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                file_size = 56, ), 
                            emoji = '', 
                            set_name = '', 
                            premium_animation = tele_rest.models.file.File(
                                file_id = '', 
                                file_unique_id = '', 
                                file_size = 56, 
                                file_path = '', ), 
                            mask_position = tele_rest.models.mask_position.MaskPosition(
                                point = 'forehead', 
                                x_shift = 1.337, 
                                y_shift = 1.337, 
                                scale = 1.337, ), 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        rarity_per_mille = 56, ), 
                    symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                        name = '', 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            emoji = '', 
                            set_name = '', 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        rarity_per_mille = 56, ), 
                    backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                        name = '', 
                        colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                            center_color = 56, 
                            edge_color = 56, 
                            symbol_color = 56, 
                            text_color = 56, ), 
                        rarity_per_mille = 56, ), 
                    publisher_chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), ),
                owned_gift_id = '',
                sender_user = tele_rest.models.user.User(
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
                send_date = 56,
                text = '',
                entities = [
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
                is_private = True,
                is_saved = True,
                can_be_upgraded = True,
                was_refunded = True,
                convert_star_count = 56,
                prepaid_upgrade_star_count = 56,
                can_be_transferred = True,
                transfer_star_count = 56,
                next_transfer_date = 56
            )
        else:
            return OwnedGift(
                type = 'unique',
                gift = tele_rest.models.unique_gift.UniqueGift(
                    base_name = '', 
                    name = '', 
                    number = 56, 
                    model = tele_rest.models.unique_gift_model.UniqueGiftModel(
                        name = '', 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            thumbnail = tele_rest.models.photo_size.PhotoSize(
                                file_id = '', 
                                file_unique_id = '', 
                                width = 56, 
                                height = 56, 
                                file_size = 56, ), 
                            emoji = '', 
                            set_name = '', 
                            premium_animation = tele_rest.models.file.File(
                                file_id = '', 
                                file_unique_id = '', 
                                file_size = 56, 
                                file_path = '', ), 
                            mask_position = tele_rest.models.mask_position.MaskPosition(
                                point = 'forehead', 
                                x_shift = 1.337, 
                                y_shift = 1.337, 
                                scale = 1.337, ), 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        rarity_per_mille = 56, ), 
                    symbol = tele_rest.models.unique_gift_symbol.UniqueGiftSymbol(
                        name = '', 
                        sticker = tele_rest.models.sticker.Sticker(
                            file_id = '', 
                            file_unique_id = '', 
                            type = 'regular', 
                            width = 56, 
                            height = 56, 
                            is_animated = True, 
                            is_video = True, 
                            emoji = '', 
                            set_name = '', 
                            custom_emoji_id = '', 
                            needs_repainting = True, 
                            file_size = 56, ), 
                        rarity_per_mille = 56, ), 
                    backdrop = tele_rest.models.unique_gift_backdrop.UniqueGiftBackdrop(
                        name = '', 
                        colors = tele_rest.models.unique_gift_backdrop_colors.UniqueGiftBackdropColors(
                            center_color = 56, 
                            edge_color = 56, 
                            symbol_color = 56, 
                            text_color = 56, ), 
                        rarity_per_mille = 56, ), 
                    publisher_chat = tele_rest.models.chat.Chat(
                        id = 56, 
                        type = 'private', 
                        title = '', 
                        username = '', 
                        first_name = '', 
                        last_name = '', 
                        is_forum = True, 
                        is_direct_messages = True, ), ),
                send_date = 56,
        )
        """

    def testOwnedGift(self):
        """Test OwnedGift"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
