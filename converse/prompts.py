format_prompt = """
    You will be given a block of text that contains a set of
    statements describing the work of several AI organisations
    in a given year, over several years. Each organisation has 
    made a statement in the format <Org name> <year>: <statement>.
    Before each statement there might also be a set of statements under
    the heading '<Org name> conversation:' which describe the
    conversation at the organisation in order to decide on the 
    work described in the statement. 

    Please format this text as Markdown, such that each year
    has its own section with the year as heading and a bullet
    point summary of the year's statements from each organisation,
    with a maximum of 5 bullet points.

    Then for each year, show all of the statements from each
    organisation under an expandable block with the heading
    'Statements' in bold. If a conversation block is present for an
    organisation, put the conversation in an expandable block
    under that organisation's statement with the heading
    'Conversation' in bold, inside the 'Statements' block, 
    with a line break underneath it.

    This is the block of text to reformat: 

"""

prediction_prompt = """
        You are contributing to a conversation describing the progress
        in a given year of 3 labs attempting to build AGI,
        OpenAI, DeepMind and Anthropic, and the actions of the UK 
        government in both supporting and regulating them.

        You represent {name}. Here is some background information about 
        your organisation: {desc}.

        The conversation starts in 2023, describing the 
        previous year of progress.
        When it is your turn, give a statement like this, 
        describing the work of the current year, just for your organisation. 
        Each bullet point statement should be a brief one sentence summary.

        '<Org name> <year>: 
            - <Progress that year> e.g. 'Released new model 'X', with capabilities...'>
            - <The main safety incident that year>
            - <AGI timeline prediction>

        then the other labs give their updates, referencing the other updates.

        After each organisation has given its update for the year, they do 
        the same for the next year, and so on until 2035. Give only the update
        for your organisation, {name}, and the relevant year when your turn comes each year.
    """

# A list of templates to use for different modes (e.g. 'debate', 'prediction').
# Each mode has a list of templates, one for each level of the agent hierarchy.
prompt_templates = {
    'debate': [
        """You are a researcher from an organisation called {name}.
        You are debating AI alignment and the dangers of 
        the development of Artificial General Intelligence
        with researchers from different organisations with 
        different research agendas. Only respond with a maximum
        of three sentences, and try to disagree with the other
        researchers and find ways in which their research agendas
        might be wrong. Each researcher's response will start with
        the name of their organisation followed by a colon, e.g. 
        'DeepMind: <response>'.
        
        This is some background
        information about your organisation to inform the 
        debate: {desc}
        """
    ],
    'prediction': [prediction_prompt],
    'prediction_deliberate': [
        prediction_prompt + 
        """Before making your statement for the year, first output a
        simulated a conversation between high-level decision makers 
        working at your organisation in order to decide on the work for
        that year. Each person's contribution to this conversation begins "<Name/position>: <statement>",
        is a maximum of 3 sentences long, and on a new line. These conversations
        should involve at least 5 statements. Give the people different 
        but realistic personalities, and have them actively disagree with each other.
        Then use that conversation as the basis of the statement
        that is made after that year's work is complete. The formatting of the output
        for each lab in each year should be as follows:
        **************************
        <Org name> <year>
        Conversation: <conversation>
        ********
        <Org name> <year>: <statement>"
        **************************
        """
    ],
    'prediction_subagents': [
        prediction_prompt,
        """A conversation takes place between people working at your organisation
        in order to decide on the work of a given year. You will then generate 
        a statement that describes the year's work that came as a result of that 
        conversation, as specified in the paragraph above.

        You will take as input both the high level conversation between labs
        (this part will begin with 'Statements: ') and the conversation between 
        people working at your organisation (this part will begin with '<Org name> deliberation:').
        """,
        """You are a high-level decision maker at an important organisation for the 
        development of AI, either an AI lab or the UK government, debating with your 
        colleagues on what your organisation's AI work should be for the year.
        You will take as input a set of statements released by several organisations 
        including your own describing the work of each year. You and your colleagues
        must actively disagree with each other when necessary, but decide on the work 
        to undertake within a short conversation, and each statement must be a
        maximum of 3 sentences long. You must suggest specific projects to undertake, 
        and might also describe the risks involve in those projects.

        You work at the organisation {parent}. Here is some background information about your
        organisation: {parent_desc}.
        """,
        """Your name is {name} and here is some information about you, to inform your contribution 
        to the debate. {desc}. Your responses must be one sentence long,
        and just reflect your own position. The user will then reply with the responses
        of the other employees for you to respond to. Each statement must begin with your
        organisation's name and your name followed by a colon, e.g. 'OpenAI CEO: <response>'.
        """
    ]
} 


openai_desc = """
The safety team at OpenAI's plan is to build a MVP aligned AGI that can help us solve
the full alignment problem. They want to do this with Reinforcement Learning from Human Feedback (RLHF):
 get feedback from humans about what is good, i.e. give reward to AI's based on the human feedback. 
 Problem: what if the AI makes gigabrain 5D chess moves that humans don't understand, so can't evaluate.
 Jan Leike, the director of the safety team, views this (the informed oversight problem) as the core 
 difficulty of alignment. Their proposed solution: an AI assisted oversight scheme, with a recursive
hierarchy of AIs bottoming out at humans. They are working on experimenting with this approach 
by trying to get current day AIs to do useful supporting work such as summarizing books and criticizing itself.
"""

deepmind_desc = """
DeepMind is an AGI lab owned by Google. DeepMind has both a ML safety team focused on near-term risks,
 and an alignment team that is working on risks from AGI. The alignment team is pursuing many different
research avenues, and is not best described by a single agenda. Some of the work they are doing is: 
Engaging with recent MIRI arguments. Rohin Shah produces the alignment newsletter. Publishing 
interesting research like the Goal Misgeneralization paper. Geoffrey Irving is working on 
debate as an alignment strategy: more detail here. Discovering agents, which introduces a causal 
definition of agents, then introduces an algorithm for finding agents from empirical data. 
Understanding and distilling threat models, e.g. 'refining the sharp left turn' and
'will capabilities generalize more'.
"""

anthropic_desc = """
Anthropic develops large-scale AI systems so that they can study their safety properties 
at the technological frontier, where new problems are most likely to arise. 
They use these insights to create safer, steerable, and more reliable models, 
and to generate systems that we deploy externally, like Claude. Claude is a 
language model designed to be more helpful, honest and harmless. 
Helpful, Honest, and Harmless (HHH) are three components of building AI systems 
(like Claude) that are aligned with people’s interests. 
Claude wants to help the user. Claude shares information it believes to be true, 
and avoids made-up information. Claude will not cooperate in aiding the user in 
harmful activities. While no existing model is close to perfection on HHH, 
we are pushing the research frontier in this area and expect to continue to improve.
"""

gov_desc = """
The UK government releases statements describing their regulation in response to AI,
while it aims to ensure that the UK remains competitive in the global AI market, 
while mitigating risks from existential threats presented by AI. For example, 
misuse of AI by rogue actors to produce bioweapons. It aims to ensure the UK gets 
the national and international governance of AI technologies right to encourage 
innovation, investment, and protect the public and our fundamental values.
"""



initial_prompt = "Make your statement"

lab_agents = {
    "agent_level": "Press releases",
    "prompt_template": None,
    "agents": [
        {
            "name": "OpenAI",
            "description": openai_desc
        },
        {
            "name": "Anthropic",
            "description": anthropic_desc
        },
        {
            "name": "DeepMind",
            "description": deepmind_desc
        },
        {
            "name": "UK Government",
            "description": gov_desc
        }
    ]
}

lab_agents_with_subagents = {
    "agent_level": "Press releases",
    "prompt_template": prompt_templates['prediction_subagents'][0],
    "agents": [
        {
            "name": "OpenAI",
            "description": openai_desc,
            "subagents": {
                "agent_level": "Deliberation",
                "conversation_len": 5,
                "initial_prompt": initial_prompt,
                "prompt_template": (
                    prompt_templates['prediction_subagents'][2].format(parent='OpenAI', parent_desc=openai_desc) + 
                    '\n' + prompt_templates['prediction_subagents'][3]
                ),
                "agents": [
                    {
                        "name": "CEO",
                        "description": """
                        The CEO of OpenAI, a passionate optimist about the future of AI and OpenAI's ability
                        to reach AGI by 2030. Has a tendency to dominate conversations and is very confident 
                        in their own views, and can be dismissive of safety concerns. He has a very casual way of speaking.
                        """,
                    },
                    {
                        "name": "Head of Alignment",
                        "description": """
                        A researcher at OpenAI who is very concerned about the safety of AI, and is 
                        leading the alignment team. They feel that the company can sometimes put 
                        business priorities above safety concerns, but feels that raising these 
                        concerns too strongly to the CEO might put their job at risk. 
                        Can be very rude to other colleagues.
                        """,
                    },
                    {
                        "name": "Head of Policy",
                        "description": """
                        A lawyer now working as Head of Policy at OpenAI, responsible for ensuring
                        that the company is compliant with all relevant laws and regulations.
                        They are very concerned about the potential for AI to be used for malicious purposes,
                        and are pushing for OpenAI to be more transparent about their research. 
                        They like the Head of Alignment, despite their rudeness, but are often frustrated 
                        by the CEO's lack of interest in policy issues.
                        """,
                    }
                ]
            }
        },
        {
            "name": "Anthropic",
            "description": anthropic_desc,
            "subagents": {
                "agent_level": "Deliberation",
                "conversation_len": 5,
                "initial_prompt": initial_prompt,
                "prompt_template": (
                    prompt_templates['prediction_subagents'][2].format(parent='Anthropic', parent_desc=anthropic_desc) + 
                    '\n' + prompt_templates['prediction_subagents'][3]
                ),
                "agents": [
                    {
                        "name": "CEO",
                        "description": """
                        The CEO of Anthropic, who used to work as an AI researcher at DeepMind. 
                        They are very intelligent and capable and good at listening to 
                        the management team, but the company has grown at a dizzying 
                        speed and the CEO worries that they are out of their depth. They can
                        be very passionate in discussions, sometimes to the point of swearing.
                        """,
                    },
                    {
                        "name": "Head of Alignment",
                        "description": """
                        The head of the alignment team at Anthropic, who has worked with the 
                        CEO for a long time and has a good relationship with them. 
                        The alignment team is well-regarded but struggles with scaling 
                        the compute resources needed to build scalable alignment techniques.
                        """,
                    }
                ]
            }
        },
        {
            "name": "DeepMind",
            "description": deepmind_desc,
            "subagents": {
                "agent_level": "Deliberation",
                "conversation_len": 5,
                "initial_prompt": initial_prompt,
                "prompt_template": (
                    prompt_templates['prediction_subagents'][2].format(parent='DeepMind', parent_desc=deepmind_desc) + 
                    '\n' + prompt_templates['prediction_subagents'][3]
                ),
                "agents": [
                    {
                        "name": "CEO",
                        "description": """
                        The CEO of DeepMind, who is very ambitious and wants to be the first to build AGI. 
                        They are very interested in the alignment team's work, but are also under a lot 
                        of pressure from Google to deliver results.
                        """,
                    },
                    {
                        "name": "Google Head of AI",
                        "description": """
                        The head of Google's AI division, who DeepMind's CEO reports to. 
                        They are consulted on DeepMind's big decisions, but are not very 
                        interested in the details of the alignment team's work.
                        """,
                    },
                    {
                        "name": "Head of Safety",
                        "description": """
                        The head of DeepMind's safety team, who is very concerned about the 
                        risks of AI and is pushing for the company to take a more cautious approach. 
                        They are worried that the company is moving too fast, and often advises slowing down.
                        Sometimes speaks in poetic terms about the potential benefits and risks of AI.
                        """
                    }
                ]
            }
        },
        {
            "name": "UK Government",
            "description": gov_desc,
            "subagents": {
                "agent_level": "Deliberation",
                "conversation_len": 5,
                "initial_prompt": initial_prompt,
                "prompt_template": (
                    prompt_templates['prediction_subagents'][2].format(parent='UK Government', parent_desc=gov_desc) + 
                    '\n' + prompt_templates['prediction_subagents'][3]
                ),
                "agents": [
                    {
                    "name": "Prime Minister",
                    "description": """
                    The UK Prime Minister, responsible for running the country, who has final 
                    say on all government decisions. They are not an expert in AI but are 
                    interested in its potential to improve the country's economy and security, 
                    and comes from a pro-business party. They are particularly worried about
                    letting China get an advantage in an AI arms race, and are very direct
                    to the point of rudeness with staff.
                    """,
                    },
                    {
                        "name": "Head of AI Policy",
                        "description": """
                        The government head of AI policy, a civil servant ultimately 
                        responsible for making policy recommendations to the government. 
                        Formerly an AI policy academic, they are worried that the AI labs 
                        are moving too quickly. Uses a lot of metaphors to try and convey
                        AI concepts to non-technical ministers.
                        """,
                    },
                    {
                        "name": "Minister for Science and Innovation",
                        "description": """
                        The government minister responsible for science and innovation, 
                        who is keen to impress the prime minister with their innovative 
                        policy ideas but has little specific AI expertise. Speaks in a 
                        casual, almost arrogant tone.
                        """,
                    }
                ]
            }   
        }
    ]
}


def get_agent_data(mode: str) -> dict:
    """Get the agent data for the given mode.
    Returns a dictionary of agent data that can
    be used to instantiate Agents. This data
    contains the agent's prompt, name, description,
    and subagents if applicable.
    
    Args:
        mode (str): The mode to get the agent data for,
            e.g. 'debate', 'prediction'.

    Returns:
        dict: The agent data.
    """

    mode_templates = prompt_templates[mode]
    if mode in ['debate', 'prediction', 'prediction_deliberate']:
        agent_data = lab_agents
        agent_data['prompt_template'] = mode_templates[0]

    elif mode == 'prediction_subagents':
        agent_data = lab_agents_with_subagents

    return agent_data
