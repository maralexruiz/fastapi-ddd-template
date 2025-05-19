class NAME_CAPITALIZED_SINGULARNotFoundError(Exception):
    message = "The NAME_LOWER_SINGULAR you specified does not exist."
    i18n = "errors.NAME_LOWER_SINGULAR_not_found"

    def __str__(self):
        return NAME_CAPITALIZED_SINGULARNotFoundError.message


class NAME_CAPITALIZED_PLURALNotFoundError(Exception):
    message = "No NAME_LOWER_PLURAL were found."
    i18n = "errors.NAME_LOWER_PLURAL_not_found"

    def __str__(self):
        return NAME_CAPITALIZED_PLURALNotFoundError.message
