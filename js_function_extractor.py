import re

# extracts it to standard code (no function)
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

# keeps it as a function, returns the function code and then the parameters
def find_js_function(js_file_path, function_name):
    with open(js_file_path, 'r') as file:
        js_code = file.read()

    pattern = r'function\s+' + function_name + r'\s*\([^)]*\)\s*{[^}]*}'
    match = re.search(pattern, js_code, re.MULTILINE | re.DOTALL)

    # search for params
    pattern = r'function\s+' + function_name + r'\s*\(([^)]*)\)\s*{[^}]*}'
    match2 = re.search(pattern, js_code, re.MULTILINE | re.DOTALL)
    

    if match:
        params = match2.group(1).split(',')
        params = [x.strip() for x in params]
        return match.group(0), params
    else:
        return None



