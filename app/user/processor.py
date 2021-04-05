from app.user.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider('user')
        self.user_id = None

    def add_id(self, user_id):
        self.user_id = user_id

    @property
    def is_exists(self):
        data = {'user_id': self.user_id}
        return bool(self.provider.is_profile_exists(data))

    def create(self, telegram_login):
        data = {
            'id': self.user_id,
            'telegram': telegram_login
        }
        return self.provider.create(data)

    def get(self):
        return self.provider.get({'id': self.user_id})

    @property
    def is_filled(self):
        user_data = self.get_register_field()
        return not (None in user_data.values())

    def update_full_name(self, full_name):
        data = {
            'id': self.user_id,
            'full_name': full_name
        }
        return self.provider.update_full_name(data)

    def update_github(self, github_link):
        data = {
            'id': self.user_id,
            'github': github_link
        }
        return self.provider.update_github(data)

    def update_phone_number(self, phone_number):
        data = {
            'id': self.user_id,
            'phone_number': phone_number
        }
        return self.provider.update_phone_number(data)

    def update_study_group(self, study_group):
        data = {
            'id': self.user_id,
            'study_group': study_group
        }
        return self.provider.update_study_group(data)
    
    def update_tshirt_size(self, tshirt_size):
        data = {
            'id': self.user_id,
            'tshirt_size': tshirt_size
        }
        return self.provider.update_tshirt_size(data)

    def update_university_name(self, university_name):
        data = {
            'id': self.user_id,
            'university_name': university_name
        }
        return self.provider.update_university_name(data)

    def update_vkontakte(self, vkontakte_link):
        data = {
            'id': self.user_id,
            'vkontakte': vkontakte_link
        }
        return self.provider.update_vkontakte(data)

    def update_email(self, email):
        data = {
            'id': self.user_id,
            'email': email
        }
        return self.provider.update_email(data)

    def get_full_name(self):
        return self.provider.get_full_name({'id': self.user_id})

    def get_github(self):
        return self.provider.get_github({'id': self.user_id})

    def get_phone_number(self):
        return self.provider.get_phone_number({'id': self.user_id})

    def get_study_group(self):
        return self.provider.get_study_group({'id': self.user_id})

    def get_tshirt_size(self):
        return self.provider.get_tshirt_size({'id': self.user_id})

    def get_university_name(self):
        return self.provider.get_university_name({'id': self.user_id})

    def get_vkontakte(self):
        return self.provider.get_vkontakte({'id': self.user_id})

    def get_email(self):
        return self.provider.get_email({'id': self.user_id})

    def get_register_field(self):
        return self.provider.get_register_field({'id': self.user_id})

    def full_name_exists(self, full_name):
        return self.provider.full_name_exists({'full_name': full_name})

    def github_exists(self, github_link):
        return self.provider.github_exists({'github': github_link})

    def phone_number_exists(self, phone_number):
        return bool(self.provider.phone_number_exists({'phone_number': phone_number}))

    def study_group_exists(self, study_group):
        return bool(self.provider.study_group_exists({'study_group': study_group}))

    def tshirt_size_exists(self, tshirt_size):
        return bool(self.provider.tshirt_size_exists({'tshirt_size': tshirt_size}))

    def university_name_exists(self, university_name):
        return bool(self.provider.university_name_exists({'university_name': university_name}))

    def vkontakte_exists(self, vkontakte_link):
        return bool(self.provider.vkontakte_exists({'vkontakte': vkontakte_link}))

    def email_exists(self, email):
        return bool(self.provider.email_exists({'email': email}))


