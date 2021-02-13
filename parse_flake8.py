import re

file_path = 'errors.txt'
lines = open(file_path).readlines()

errors = {}

for line in lines:
    line = line.strip()
    gr = re.match(r"""^(.*?):(\d+):(\d+):(\s*)(\S*)(.*?)$""", line)
    err_file = gr.group(1)
    err_line = int(gr.group(2))
    err_pos = int(gr.group(3))
    err_code = gr.group(5)
    err_text = gr.group(6).strip()
    #print(err_code, err_text)
    gr = re.match("""^([A-Z]+)([0-9]+)$""", err_code)
    err_code_pref = gr.group(1)
    if err_code_pref not in errors:
        errors[err_code_pref] = dict()
    if err_code not in errors[err_code_pref]:
        errors[err_code_pref][err_code] = []
    errors[err_code_pref][err_code].append({
        "err_file": err_file,
        "err_line": err_line,
        "err_pos": err_pos,
        "err_text": err_text,
    })


for err_code_pref in errors:
    print(f"Error group {err_code_pref}")
    for err_code in errors[err_code_pref]:
        print(f"    Error subgroup {err_code}")
        for item in errors[err_code_pref][err_code]:
            print(f"        {item['err_file']}:{item['err_line']}:{item['err_pos']}: {item['err_text']}")
