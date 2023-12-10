class PyToJSTranspiler:
    def __init__(self):
        self.translations = {
            'click': self.translate_click,
            'set_value': self.translate_set_value,
            'get_value': self.translate_get_value,
            'write_element': self.translate_write_element,  # Add this line
        }

    def translate(self, command, *args):
        if command in self.translations:
            return self.translations[command](*args)
        raise NotImplementedError(f"Command '{command}' not implemented in transpiler.")

    def translate_click(self, selector):
        return f"document.querySelector('{selector}').click();"

    def translate_set_value(self, selector, value):
        return f"document.querySelector('{selector}').value = `{value}`;"

    def translate_get_value(self, selector):
        return f"const value = document.querySelector('{selector}').value; return value;"

    def translate_write_element(self, selector, text):
        return f"document.querySelector('{selector}').innerText = `{text}`;"
