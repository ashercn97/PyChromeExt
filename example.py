from core import PyChromeExt, Permission, ContentScript, Website
from py_to_js_transpiler import PyToJSTranspiler
from flask import Flask
from flask_cors import CORS
import threading


app = Flask(__name__)
CORS(app)


extension = PyChromeExt(app, "ExampleModifier", "1.0")
transpiler = PyToJSTranspiler()

# Define permissions for example.com
example_perm = Permission(["https://ashercn97.github.io/WebsiteForRasppi/*"])
extension.add_permission(example_perm)

# Create a Website instance for interactions on example.com
example_website = Website(transpiler)
example_website.add_interaction('write_element_by_id', 'yay', 'Hello world!')
example_website.add_interaction('read_element_by_id', 'yay')



def do_stuff_with_yay_read(data):
    global yay_read
    yay_read = data
    print(yay_read)
    #print(yay_read)
    # Any other processing you need
    # If you need to do asynchronous tasks here, consider using a task queue like Celery


# Set up the data receiver with the callback
extension.setup_data_receiver('/receive_data', 'yay_read', do_stuff_with_yay_read)


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