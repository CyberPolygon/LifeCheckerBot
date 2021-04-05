from app.base.provider import BaseProvider


class Provider(BaseProvider):
    def __int__(self, sql_path):
        super().__init__(sql_path)

    def is_profile_exists(self, data):
        return self.exec_by_file('exists/user.sql', data)[0].get('count')

    def create(self, data):
        return self.exec_by_file('create.sql', data)[0].get('id')

    def get(self, data):
        return self.exec_by_file('get/user.sql', data)[0]

    def update_full_name(self, data):
        return self.exec_by_file('update/user_full_name.sql', data)

    def update_phone_number(self, data):
        return self.exec_by_file('update/user_phone_number.sql', data)

    def update_github(self, data):
        return self.exec_by_file('update/user_github.sql', data)

    def update_email(self, data):
        return self.exec_by_file('update/user_email.sql', data)

    def update_vkontakte(self, data):
        return self.exec_by_file('update/user_vkontakte.sql', data)

    def update_university_name(self, data):
        return self.exec_by_file('update/user_university_name.sql', data)

    def update_tshirt_size(self, data):
        return self.exec_by_file('update/user_tshirt_size.sql', data)

    def update_study_group(self, data):
        return self.exec_by_file('update/user_study_group.sql', data)

    def get_register_field(self, data):
        return self.exec_by_file('get/user_register_fields.sql', data)[0]

    def get_full_name(self, data):
        return self.exec_by_file('get/user_full_name.sql', data)[0].get('full_name')

    def get_phone_number(self, data):
        return self.exec_by_file('get/user_phone_number.sql', data)[0].get('phone_number')

    def get_github(self, data):
        return self.exec_by_file('get/user_github.sql', data)[0].get('github')

    def get_email(self, data):
        return self.exec_by_file('get/user_email.sql', data)[0].get('email')

    def get_vkontakte(self, data):
        return self.exec_by_file('get/user_vkontakte.sql', data)[0].get('vkontakte')

    def get_university_name(self, data):
        return self.exec_by_file('get/user_university_name.sql', data)[0].get('university_name')

    def get_tshirt_size(self, data):
        return self.exec_by_file('get/user_tshirt_size.sql', data)[0].get('tshirt_size')

    def get_study_group(self, data):
        return self.exec_by_file('get/user_study_group.sql', data)[0].get('study_group')

    def full_name_exists(self, data):
        return self.exec_by_file('exists/user_full_name.sql', data)[0].get('count')

    def phone_number_exists(self, data):
        return self.exec_by_file('exists/user_phone_number.sql', data)[0].get('count')

    def github_exists(self, data):
        return self.exec_by_file('exists/user_github.sql', data)[0].get('count')

    def email_exists(self, data):
        return self.exec_by_file('exists/user_email.sql', data)[0].get('count')

    def vkontakte_exists(self, data):
        return self.exec_by_file('exists/user_vkontakte.sql', data)[0].get('count')

    def university_name_exists(self, data):
        return self.exec_by_file('exists/user_university_name.sql', data)[0].get('count')

    def tshirt_size_exists(self, data):
        return self.exec_by_file('exists/user_tshirt_size.sql', data)[0].get('count')

    def study_group_exists(self, data):
        return self.exec_by_file('exists/user_study_group.sql', data)[0].get('count')
