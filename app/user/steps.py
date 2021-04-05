from app.config import bot
from app.user.processor import Processor as UserProcessor
import re

user = UserProcessor()


def processor_dispatcher(message):
    user_id = message.chat.id
    user_data = user.get()

    if not user_data.get('full_name'):
        bot.send_message(user_id, "Введите своё ФИО в формате: Фамилия Имя Отчество.")
        bot.register_next_step_handler(message, process_full_name)

    elif not user_data.get('email'):
        bot.send_message(user_id, "Введите свой email в формате: some-test@example.com")
        bot.register_next_step_handler(message, process_email)

    elif not user_data.get('phone_number'):
        bot.send_message(user_id, "Введите свой номер телефона в формате: +79835552316")
        bot.register_next_step_handler(message, process_phone_number)

    elif not user_data.get('university_name'):
        bot.send_message(user_id, "Введите своё название ВУЗа высоким регистром.")
        bot.register_next_step_handler(message, process_university_name)

    elif not user_data.get('study_group'):
        bot.send_message(user_id, "Введите свою учебную группу в формате АБВ-195")
        bot.register_next_step_handler(message, process_study_group)

    elif not user_data.get('tshirt_size'):
        bot.send_message(user_id, "Введите свой размер футболки из доступных: S, M, L, XL, XXL, XXXL")
        bot.register_next_step_handler(message, process_tshirt_size)

    elif not user_data.get('vkontakte'):
        bot.send_message(user_id, "Введите свою ссылку на вконтакте по примеру: https://vk.com/madwayz1337")
        bot.register_next_step_handler(message, process_vkontakte)

    elif not user_data.get('github'):
        bot.send_message(user_id, "Введите свою ссылку на github.com по примеру: https://github.com/madwayz1337")
        bot.register_next_step_handler(message, process_github)
    else:
        bot.send_message(user_id, 'Спасибо! Все данные успешно внесены в базу данных. '
                                  'Используйте /help для получения информации о командах.')


def start_register(message):
    user_id = message.chat.id
    user.add_id(user_id)

    if not user.is_exists:
        user_id = user.create(telegram_login=message.chat.username)
        if not user_id:
            return bot.send_message(user_id, "Возникла ошибка при регистрации. Попробуйте позже.")

        bot.send_message(user_id, "Аккаунт зарегистрирован. Осталось только заполнить поля")

    if not user.is_filled:
        return processor_dispatcher(message)

    return bot.send_message(user_id, 'Аккаунт уже зарегистрирован и сведения заполнены.')


def process_full_name(message):
    re_format = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата ФИО. Введите примеру: Фамилия Имя Отчество')
        bot.register_next_step_handler(msg, process_full_name)
        return

    user.update_full_name(message.text)
    processor_dispatcher(message)


def process_email(message):
    # Добавить проверку почты на владение.
    re_format = r'^[\w.-]+@[\w.-]+\.[\w.-]+$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата e-mail. Введите примеру: some-test@example.com')
        bot.register_next_step_handler(msg, process_email)
        return

    if user.get_email():
        msg = bot.send_message(message.chat.id, 'Такой e-mail уже есть в базе. Введите другой.')
        bot.register_next_step_handler(msg, process_email)
        return

    user.update_email(message.text)
    processor_dispatcher(message)


def process_university_name(message):
    re_format = r'^[А-ЯЁ]+$'

    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата названия учебного заведения. '
                                                'Введите по примеру: СИБГУТИ')
        bot.register_next_step_handler(msg, process_university_name)
        return

    user.update_university_name(message.text)
    processor_dispatcher(message)


def process_study_group(message):
    re_format = r'^[А-ЯЁ]+\-\d+$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата названия учебной группы. Введите по примеру: АБВ-195')
        bot.register_next_step_handler(msg, process_study_group)
        return

    user.update_study_group(message.text)
    processor_dispatcher(message)


def process_phone_number(message):
    re_format = r'^\+7\d{10}$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата номера телефона '
                                                'Введите по примеру: +79835552316')
        bot.register_next_step_handler(msg, process_phone_number)
        return

    if user.get_phone_number():
        msg = bot.send_message(message.chat.id, 'Такой номер телефона уже есть в базе. Введите другой.')
        bot.register_next_step_handler(msg, process_phone_number)
        return

    user.update_phone_number(message.text)
    processor_dispatcher(message)


def process_tshirt_size(message):
    re_format = r'^S|M|L|XL|XXL|XXXL$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата названия учебного заведения. '
                                                'Выберите из списка и введите размер футболки: S, M, L, XL, XXL, XXXL')
        bot.register_next_step_handler(msg, process_tshirt_size)
        return

    user.update_tshirt_size(message.text)
    processor_dispatcher(message)


def process_vkontakte(message):
    re_format = r'^https?:\/\/vk.com\/[\w.-]+$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата ссылки на ВКонтакте. '
                                                'Введите по примеру: https://vk.com/madwayz1337')
        bot.register_next_step_handler(msg, process_vkontakte)
        return

    if user.vkontakte_exists(message.text):
        msg = bot.send_message(message.chat.id, 'Такая ссылка уже есть в базе. Введите другую.')
        bot.register_next_step_handler(msg, process_vkontakte)
        return

    user.update_vkontakte(message.text)
    processor_dispatcher(message)


def process_github(message):
    re_format = r'^https?:\/\/github.com\/[\w.-]+$'
    if not re.findall(re_format, message.text):
        msg = bot.send_message(message.chat.id, 'Ошибка формата ссылки на github.com '
                                                'Введите спо примеру: https://github.com/madwayz1337')
        bot.register_next_step_handler(msg, process_github)
        return

    if user.github_exists(message.text):
        msg = bot.send_message(message.chat.id, 'Такая ссылка уже есть в базе. Введите другую.')
        bot.register_next_step_handler(msg, process_vkontakte)
        return

    processor_dispatcher(message)
