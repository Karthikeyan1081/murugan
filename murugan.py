
import os , requests, re , json
apiKey = "c64b6bee-da01-48d6-9246-092d3f79664f"
def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter date", "type": "text"}, {"id": "{input_2}", "label": "Enter loads", "type": "text"}, {"id": "{input_3}", "label": "Enter counts", "type": "text"}, {"id": "{input_4}", "label": "Enter import", "type": "text"}, {"id": "{input_5}", "label": "Enter export", "type": "text"}, {"id": "{input_6}", "label": "Enter advance", "type": "text"}, {"id": "{input_7}", "label": "Enter tea price", "type": "text"}, {"id": "{input_8}", "label": "Enter diesel", "type": "text"}]
    prompt = "Calculate the salary based on the given inputs: date {input_1}, loads {input_2}, counts {input_3}, import {input_4}, export {input_5}, advance {input_6}, tea price {input_7}, diesel {input_8}. The salary is calculated as counts*0.13, extra as loads*150, and total amount as salary+extra. The output should be returned in the form of a table or excel sheet format."
    filesData, textData = {}, {}
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            f = open(path, 'rb')
            filesData[inputId] = f

    textData['details'] = json.dumps({'appname': 'salary calculator 1','prompt': prompt,'documentId': 'no-embd-type','appId' : '66c9cd5264d827b744a2a1d3' , 'memoryId' : '','apiKey': apiKey})
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']
usersInputObj = {'{input_1}' : input("Enter date "),'{input_2}' : input("Enter loads "),'{input_3}' : input("Enter counts "),'{input_4}' : input("Enter import "),'{input_5}' : input("Enter export "),'{input_6}' : input("Enter advance "),'{input_7}' : input("Enter tea price "),'{input_8}' : input("Enter diesel "),}
output = apiFunction(usersInputObj)
url_regex = r'http://localhost:7000/'
replaced_string = re.sub(url_regex,'https://apiappstore.guvi.ai/' , output)
print(replaced_string)
