from core import PyChromeExt, Permission, ContentScript, Website
from py_to_js_transpiler import PyToJSTranspiler
from flask import Flask

app = Flask(__name__)
extension = PyChromeExt(app, "ExampleModifier", "1.0")
transpiler = PyToJSTranspiler()

# Define permissions for example.com
example_perm = Permission(["https://www.example.com/*"])
extension.add_permission(example_perm)

# Create a Website instance for interactions on example.com
example_website = Website(transpiler)
example_website.add_interaction('write_element', "h1", 'Modified by PyChromeExt!')


# Define a content script for example.com
example_script = ContentScript(
    match_patterns=["https://www.example.com/"],
    website=example_website
)
extension.add_content_script(example_script)

# Build extension files
extension.build_extension_files(output_dir="example_extension_files")

if __name__ == "__main__":
    app.run(debug=True)
