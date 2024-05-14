from django.contrib.auth.models import BaseUserManager

from util.encoder import encode_md5


class OnlineShopUserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password):
        if not email:
            raise ValueError('Email is required')
        if not full_name:
            raise ValueError('Full_Name is required')

        user = self.model(email=self.normalize_email(email), phone_number=phone_number, full_name=full_name)

        encoded_password = encode_md5(password)

        user.set_password(encoded_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, password):
        user = self.create_user(email, full_name, phone_number, password)

        user.is_admin = True
        user.save(using=self._db)
        return user
