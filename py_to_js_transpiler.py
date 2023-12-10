class PyToJSTranspiler:
    def __init__(self):
        self.translations = {
            'click': self.translate_click,
            'set_value': self.translate_set_value,
            'get_value': self.translate_get_value,
            'write_element': self.translate_write_element,  # Add this line
            'read_element_by_id': self.translate_read_element_by_id,  # Add this line
            'set_element_by_id': self.translate_set_element_by_id,    # Add this line
            'write_element_by_id': self.translate_write_element_by_id, # Add this line
            'read_element_by_class': self.translate_read_element_by_class,
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

    def translate_read_element_by_id(self, element_id):
        return f"""
        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://localhost:5000/receive_data', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({{ 'data': document.getElementById('{element_id}').innerText }}));
        """

    def translate_set_element_by_id(self, element_id, value):
        return f"document.getElementById('{element_id}').value = `{value}`;"

    def translate_write_element_by_id(self, element_id, text):
        return f"document.getElementById('{element_id}').innerText = `{text}`;"


    def translate_read_element_by_class(self, class_name):
            return f"""
            var elements = document.getElementsByClassName('{class_name}');
            var data = [];
            for (var i = 0; i < elements.length; i++) {{
                data.push(elements[i].innerText);
            }}
            var xhr = new XMLHttpRequest();
            xhr.open("POST", 'http://localhost:5000/receive_data', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({{'data': data}}));
            """
