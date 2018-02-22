"""
Contains code that gets run inside our mako template
Debugging python-in-mako is terrible, so we've moved the actual code out to its own file
"""

def load_sfe_i18n_data(locale):
    """
    Loads i18n data from studio-frontend's published files.
    """
    messages = "{}"
    locale_data = ""

    if locale != 'en':
        # because en is the default, studio-frontend will have it loaded by default
        messages_path = "{base}/studio-frontend/dist/i18n/messages/{locale}.json".format(
            base=settings.STATIC_ROOT_BASE,
            locale=locale.replace('-', '_')  # files from Transifex use _, platform follows RFC-5646 and uses -
        )
        with open(messages_path) as inputfile:
            messages = inputfile.read()

        locale_data_path = "{base}/studio-frontend/dist/i18n/locale_data/{locale}.js".format(
            base=settings.STATIC_ROOT_BASE,
            locale=locale.split('-')[0]  # extended language information is located in the primary language file
        )
        with open(locale_data_path) as inputfile:
            locale_data = inputfile.read()

        """
        If we don't escape internal quotes here, the browser may interpret the (valid javascript) contents of
        locale_data to be javascript, which causes errors. Escaping them still allows for a successful parse by SFE on
        the other end.
        """
        locale_data.replace('\"', '\\\"')

    return messages, locale_data
