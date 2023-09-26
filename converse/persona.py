import openai


class Persona(object):

    def __init__(self, name, description, prompt_template) -> None:
        self.name = name
        system_prompt = prompt_template.format(name=name, desc=description)
        self.messages = [{'role': 'system', 'content': system_prompt}]
    
    def get_response(self, input, model='gpt-4'):
        self.messages.append({'role': 'user', 'content': input})
        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages,
            temperature=1.0
        )
        newest = response.choices[0].message
        self.messages.append(newest)

        return newest['content']
