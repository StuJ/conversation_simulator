# Run the conversation between agents, coordinating
# hierarchical discussions where the high level agent
# summarises the conversation between sub agents, and
# the sub agents generate their own statement.
import os
import pathlib

import prompts
import agent
import converse


def handle():
    """Handle the conversation between agents."""

    run_name='7-government-annual'
    prompt_template = prompts.prompt_templates['prediction']

    conversation = converse.run_conversation(
        agents=agent.instantiate_agents(prompts.agent_data, prompt_template), 
        initial_prompt='Begin the conversation', 
        prompt_template=prompt_template, 
        conversation_length=20,
        model='gpt-4', 
        deliberate=True
    )

    output_fname = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        f'conversations/{run_name}.txt'
    )

    with open(output_fname, 'w+') as f:
        f.write('\n\n'.join(conversation))

    print(f'Written output to {output_fname}.')


if __name__ == '__main__':
    handle()
