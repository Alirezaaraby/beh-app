# validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    UserAttributeSimilarityValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
)

class CustomPasswordValidator:
    def __init__(self):
        self.validators = [
            MinimumLengthValidator(min_length=8),
            UserAttributeSimilarityValidator(),
            CommonPasswordValidator(),
            NumericPasswordValidator(),
        ]

    def validate(self, password, user=None):
        errors = []
        for validator in self.validators:
            try:
                validator.validate(password, user)
            except ValidationError as e:
                for error in e.error_list:
                    # Customize error messages here
                    if error.code == 'password_too_short':
                        error.message = _("این رمز عبور خیلی کوتاه است. باید حداقل ۸ کاراکتر داشته باشد.")
                    elif error.code == 'password_too_similar':
                        error.message = _("رمز عبور خیلی شبیه به اطلاعات شخصی شما است.")
                    elif error.code == 'password_too_common':
                        error.message = _("این رمز عبور خیلی رایج است.")
                    elif error.code == 'password_entirely_numeric':
                        error.message = _("این رمز عبور کاملاً عددی است.")
                errors.extend(e.error_list)
        if errors:
            # print(errors)
            raise ValidationError(errors)

    def get_help_text(self):
        help_texts = [validator.get_help_text() for validator in self.validators]
        # print(help_texts)
        return " ".join(help_texts)