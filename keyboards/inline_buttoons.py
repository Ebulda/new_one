from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        'Registration',
        callback_data='fsm_start'
    )
    my_profile_button = InlineKeyboardButton(
        'My profile',
        callback_data='my_profile'
    )
    random_profile_button = InlineKeyboardButton(
        'View profile',
        callback_data='random_profile'
    )
    reference_menu_button = InlineKeyboardButton(
        'Referral Menu',
        callback_data='reference_menu'
    )
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
    markup.add(reference_menu_button)
    return markup

async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        'Like',
        callback_data=f'user_form_like_{owner_tg_id}'
    )
    user_form_dislike_button = InlineKeyboardButton(
        'Dislike',
        callback_data='random_profile'
    )
    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        'Referral Link',
        callback_data='reference_link'
    )
    reference_list_button = InlineKeyboardButton(
        "Referral List 🗒️",
        callback_data="reference_list"
    )
    markup.add(reference_link_button)
    markup.add(reference_list_button)
    return markup
