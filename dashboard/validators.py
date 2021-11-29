from django.core.exceptions import ValidationError

def validate_image_size(value):
    filesize= value.size
    if filesize > 2621440:
        raise ValidationError("The maximum file size that can be uploaded is 2.5 MB")
    else:
        return value