# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import agent, converse, prompts, utils


def handle():
    """Handle the conversation between agents."""

    # Running with China but no subagents.
    # Keep doing this for more variants - I've already demonstrated subagent ability.
    conversation_length = 30
    run_name = f'15-china-len-{conversation_length}'
    mode = 'prediction'
    agent_data = prompts.get_agent_data(mode)

    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=conversation_length,
        model='gpt-4-1106-preview',
        subagent_conv=False
    )
    output = utils.format_output(conversation)

    output_dir = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        f'conversations/{mode}'
    )
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_fname = os.path.join(output_dir, f'{run_name}.md')

    with open(output_fname, 'w+') as f:
        f.write(output)

    print(f'Written output to {output_fname}.')


if __name__ == '__main__':
    handle()
