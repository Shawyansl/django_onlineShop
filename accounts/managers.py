from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def normalize_email(self, email):
        return email.lower()
    
    def normalize_phone(self, phone):
        return phone

    def create_user(self, email, phone, password, **extra_fields):
        if email and phone:
            email = self.normalize_email(email)
            phone = self.normalize_phone(phone)

            user  = self.model(email=email , phone=phone , **extra_fields)
            user.set_password(password)
            user.save()
        else:
            raise ValueError("email and phone must be set.")
    
    def create_superuser(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, phone, password, **extra_fields)