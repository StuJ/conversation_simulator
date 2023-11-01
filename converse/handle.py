# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import prompts
import agent
import converse


def handle():
    """Handle the conversation between agents."""

    run_name='8-deliberate'
    mode = 'prediction_deliberate'
    agent_data = prompts.get_agent_data(mode)

    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=20,
        model='gpt-4',
        subagent_conv=False
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
