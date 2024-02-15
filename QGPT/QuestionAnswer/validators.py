from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.template.defaultfilters import filesizeformat


class FileSizeValidator(BaseValidator):
    one_megabyte = 1048576

    def __init__(self, max_size=one_megabyte * 10):
        self.max_size = max_size
        ...

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(
                f"File size shouldn't exceed {filesizeformat(self.max_size)}"
            )
