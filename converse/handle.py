# Run the conversation between agents, coordinating
# hierarchical discussions where the high level agent
# summarises the conversation between sub agents, and
# the sub agents generate their own statement.

import prompts
import agent
import converse


def handle():
    """Run the conversation between agents."""

    prompt_template = prompts.prompt_templates['prediction']

    converse.run_conversation(
        agents=agent.instantiate_agents(prompts.agent_data, prompt_template), 
        initial_prompt='Begin the conversation', 
        prompt_template=prompt_template, 
        run_name='7-government-annual', 
        conversation_length=20,
        model='gpt-4', 
        deliberate=True
    )


if __name__ == '__main__':
    handle()
