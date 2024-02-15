from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from .validators import file_size_validator


def file_size_validator(value, max_size=None):
    one_megabyte = 1048576 
    
    if max_size is None: # set 10-megabytes as max size default
        max_size = one_megabyte * 10 
    if value.size > max_size:
        raise ValidationError(f"File size shouldn't exceed {filesizeformat(max_size)}")