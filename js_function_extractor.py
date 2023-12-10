import re

def extract_js_function(js_file_path, function_name, params):
    with open(js_file_path, 'r') as file:
        js_code = file.read()

    # Regular expression to find the function
    pattern = rf"function {function_name}\((.*?)\)\s*\{{(.*?)\}}"
    match = re.search(pattern, js_code, re.DOTALL)

    if match:
        param_list = match.group(1).split(',')
        function_body = match.group(2).strip()

        # Replace parameters with provided values
        for i, param in enumerate(param_list):
            if i < len(params):
                function_body = function_body.replace(param.strip(), params[i])

        return function_body

    return None