from core import PyChromeExt, Permission, ContentScript, Website, Function
from py_to_js_transpiler import PyToJSTranspiler
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


extension = PyChromeExt(app, "ExampleComponent", "1.0")
transpiler = PyToJSTranspiler()

# Define permissions for example.com
example_perm = Permission(["https://ashercn97.github.io/WebsiteForRasppi/*"])
extension.add_permission(example_perm)

# Create a Website instance for interactions on example.com
example_website = Website(transpiler)

'''

example_website.add_interaction('read_element_by_id', 'yay')


def callback(data):
    print(data)

# Set up the data receiver with the callback
extension.setup_data_receiver('/receive_data', 'yay_read', callback)


# Define a content script for example.com
example_script = ContentScript(
    match_patterns=["https://ashercn97.github.io/WebsiteForRasppi/"],
    website=example_website
)
extension.add_content_script(example_script)

# Build extension files
extension.build_extension_files(output_dir="example_extension_files")

if __name__ == "__main__":
    app.run()
    '''

# define a function
console_log = Function('./content_script_utils.js', 'console_log')

example_website.add_function(console_log)
example_website.call_function('console_log', message="Hello world!")


# Define a content script for example.com
example_script = ContentScript(
    match_patterns=["https://ashercn97.github.io/WebsiteForRasppi/"],
    website=example_website
)
extension.add_content_script(example_script)

# Build extension files
extension.build_extension_files(output_dir="example_extension_files")

if __name__ == "__main__":
    app.run()