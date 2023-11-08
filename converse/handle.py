# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import prompts
import agent
import converse


def format_output(conversation: list[str]) -> str:
    pass


def handle():
    """Handle the conversation between agents."""

    run_name='8-deliberate'
    mode = 'prediction_subagents'
    agent_data = prompts.get_agent_data(mode)

    # openai.error.RateLimitError: Rate limit reached for gpt-4 in organization org-7W50jQPbaFHstUhw4AmRpxMx on tokens per min. Limit: 10000 / min. Please try again in 6ms. Visit https://platform.openai.com/account/rate-limits to learn more.
    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=20,
        model='gpt-3.5-turbo',
        subagent_conv=True
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
