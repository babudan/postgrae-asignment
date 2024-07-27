


class ValidationException(Exception):
    pass


class Validation:
    @staticmethod
    def validate_field(name ,parameter_value):
        if not name or name == '':
            raise ValidationException(f'{parameter_value} field is missing.')
        return True
