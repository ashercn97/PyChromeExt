from js_function_extractor import extract_js_function

class Permission:
    def __init__(self, urls):
        self.urls = urls

class Website:
    def __init__(self, transpiler):
        self.interactions = []
        self.transpiler = transpiler

    def add_interaction(self, command, *args):
        js_code = self.transpiler.translate(command, *args)
        self.interactions.append(js_code)

    def read_element(self, selector):
        self.interactions.append(f"const text = document.querySelector('{selector}').innerText;")
        return "text"


    def write_element(self, selector, value):
        self.interactions.append(f'document.querySelector("{selector}").innerText = `{value}`;')

    def click_element(self, selector):
        self.interactions.append(f"document.querySelector('{selector}').click();")

    def set_element_value(self, selector, value):
        self.interactions.append(f"document.querySelector('{selector}').value = `{value}`;")
    
    def add_custom_interaction(self, interaction_code):
        self.interactions.append(interaction_code)

    def get_value(self, selector):
        js_code = self.transpiler.translate('get_value', selector)
        self.interactions.append(js_code)
        return "value"

    def generate_script(self):
        return "setTimeout(() => { \n" + "\n".join(self.interactions) + "\n  }, 1000);"

class ContentScript:
    def __init__(self, match_patterns, website):
        self.match_patterns = match_patterns
        self.website = website

    def generate_script(self):
        return f"// Content Script for: {self.match_patterns}\n{self.website.generate_script()}"

class PyChromeExt:
    def __init__(self, app, extension_name, extension_version):
        self.app = app
        self.extension_name = extension_name
        self.extension_version = extension_version
        self.permissions = []
        self.content_scripts = []

    def add_permission(self, permission):
        self.permissions.extend(permission.urls)

    def add_content_script(self, content_script):
        self.content_scripts.append(content_script)

    def generate_manifest_data(self):
        manifest = {
            "manifest_version": 2,
            "name": self.extension_name,
            "version": self.extension_version,
            "permissions": self.permissions,
            "content_scripts": [{
                "matches": script.match_patterns,
                "js": ["content.js"]
            } for script in self.content_scripts],
            "background": {
                "scripts": ["background.js"],
                "persistent": False
            }
        }
        return manifest

    def generate_content_script(self):
        content_script_code = "\n"
        for script in self.content_scripts:
            content_script_code += script.generate_script() + "\n\n"
        return content_script_code

    def generate_background_script(self):
        return "chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {\n" \
               "    // Add your background script logic here\n" \
               "});"

    def build_extension_files(self, output_dir):
        import os
        import json

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(os.path.join(output_dir, 'manifest.json'), 'w') as file:
            json.dump(self.generate_manifest_data(), file, indent=4)

        with open(os.path.join(output_dir, 'content.js'), 'w') as file:
            file.write(self.generate_content_script())

        with open(os.path.join(output_dir, 'background.js'), 'w') as file:
            file.write(self.generate_background_script())

    def add_content_script(self, content_script):
        self.content_scripts.append(content_script)


    def add_dynamic_content_script(self, match_patterns, interaction_code):
        website = Website()
        website.add_custom_interaction(interaction_code)
        self.add_content_script(ContentScript(match_patterns, website))

    def add_js_function_from_file(self, js_file_path, function_name, params, match_patterns):
        js_function_code = extract_js_function(js_file_path, function_name, params)
        if js_function_code:
            website = Website()
            website.add_custom_interaction(js_function_code)
            self.add_content_script(ContentScript(match_patterns, website))
