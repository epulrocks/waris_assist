from http import HTTPStatus
from dashscope import Application
import dashscope
import json

class WarisAssist():
    def __init__(self, api_key=None, app_id=None):
        self.api_key = api_key
        self.app_id = app_id
        self.session_id = None
        dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

    def clean_json(self, json_string):
        json_string = json_string[7:-3]
        json_string = json_string.replace("\n", "")
        return json.loads(json_string)

    def chat(self, prompt):
        response = Application.call(
            # If environment variables are not configured, you can replace the following line with api_key="sk-xxx". However, it is not recommended to hard code the API Key directly into the code in a production environment to reduce the risk of API Key leakage.
            api_key=self.api_key,
            app_id=self.app_id,# Replace with the actual application ID
            prompt=prompt,
            session_id=self.session_id
        )

        if response.status_code != HTTPStatus.OK:
            print(f'request_id={response.request_id}')
            print(f'code={response.status_code}')
            print(f'message={response.message}')
            print(f'Refer to: https://www.alibabacloud.com/help/en/model-studio/developer-reference/error-code')
            raise Exception(f'Error: {response.status_code} - {response.message}')
        elif response.output.text[:7] != "```json":
            raise Exception(f"Response is not in JSON format\n{response.output.text}")
        else:
            json_response = self.clean_json(response.output.text)
            self.session_id = response.output.session_id
            return json_response
        
if __name__ == "__main__":
    import os
    test = WarisAssist(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        app_id=os.getenv("APP_ID")
    )
    resp = test.chat("what is the process to get death certificate in Malaysia")