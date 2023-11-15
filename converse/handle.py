# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import agent, converse, prompts, utils


def handle():
    """Handle the conversation between agents."""

    conversation_length = 30
    run_name = f'13-subagent-no-gov-len-{conversation_length}'
    mode = 'prediction_subagents'
    agent_data = prompts.get_agent_data(mode)

    # TODO: just see if it did cut off because of token limit.
    # if finish_reason is 'stop', prompt again saying 'please continue'.
    # Or just not bother formatting longer conversations
    # or write a script to do it
    # Could then try and get GPT4 to score each conversation
    # according to capability and risk, then run a bunch under
    # different circumstances and see how they score.

    # Or just run as long as possible and then format the output
    # and run experiments on that time frame.
    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=conversation_length,
        model='gpt-4-1106-preview',
        subagent_conv=True
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
