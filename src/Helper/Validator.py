from flask import current_app
import re


def validate_password(password: str) -> (bool, str):
    """
    Check if the password follows the rules.

    :param password: The password to validate.
    :returns:
              - bool: True if the password is valid, False otherwise.
              - str: The reason in case the password is invalid.
    :rtype: tuple
    """
    # Minimum length
    if len(password) < current_app.config["PASSWORD_MINIMUM_LENGTH"]:
        return False, f"Password must be at least {current_app.config['PASSWORD_MINIMUM_LENGTH']} characters long."

    # Contains at least one lowercase letter
    if current_app.config["PASSWORD_MUST_CONTAIN_LOWER_CASE"] and not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    # Contains at least one uppercase letter
    if current_app.config["PASSWORD_MUST_CONTAIN_UPPER_CASE"] and not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    # Contains at least one digit
    if current_app.config["PASSWORD_MUST_CONTAIN_DIGIT"] and not re.search(r'\d', password):
        return False, "Password must contain at least one digit."

    # Contains at least one special character
    if current_app.config["PASSWORD_MUST_CONTAIN_SPECIAL_CHARACTER"] \
            and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password is valid."


def validate_email(email: str) -> bool:
    """
    Check if the email is valid or not. The email must be in the format email@domain.
    :param email: The email address to validate.
    :return: True if the email is valid, False otherwise.
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True
