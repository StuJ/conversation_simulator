import os
import pathlib
import itertools

import openai

import prompts
from persona import Persona

openai.api_key = os.getenv("OPENAI_API_KEY")



def run_conversation(initial_prompt, prompt_template, run_name, conversation_length, model):
    # V2 - take an arbitrary number of personas and have each consume the whole conversation
    # since they last spoke, then take turns speaking.

    # Instantiate personas.
    personas = [
        Persona(
            name=entry['name'],
            description=entry['description'],
            prompt_template=prompt_template
        ) 
        for entry in prompts.persona_data
    ]

    conversation = [initial_prompt]
    # Loop through personas, passing output of one to input of other.

    # Save next input responses for each persona.
    next_input_responses = {persona.name: [] for persona in personas}

    # For each persona, feed the comments since they last spoke 
    # as user input to their response.
    for persona in itertools.cycle(personas):

        if len(next_input_responses[persona.name]) > 0:
            input_responses = '\n'.join(next_input_responses[persona.name])
            next_input_responses[persona.name] = []
        else:
            input_responses = initial_prompt

        response = persona.get_response(input_responses, model)
        print(f'{response}\n')

        for name in next_input_responses.keys():
            if name != persona.name:
                next_input_responses[name].append(response)

        conversation.append(response)
        if len(conversation) >= conversation_length:
            break

    output_fname = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        f'conversations/{run_name}.txt'
    )

    with open(output_fname, 'w+') as f:
        f.write(prompt_template + '\n\n'.join(conversation))

    print(f'Written output to {output_fname}.')


def run():
    # Be able to choose modes, e.g. debate or predicting actions
    # Why chat completion instead of normal completion?
    # Can give each contributor more individual context and save their
    # state? Easier to scale, rather than giving massive initial prompt
    # with loads of background info. Better simulates separate actors.

    run_name = '7-government-annual'
    initial_prompt = 'Begin the conversation'
    prompt_template = prompts.prompt_templates['prediction']
    conversation_length = 20
    model = 'gpt-4'

    run_conversation(initial_prompt, prompt_template, run_name, conversation_length, model)


if __name__ == '__main__':
    run()
