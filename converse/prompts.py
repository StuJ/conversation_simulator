prompt_templates = {
    'debate': """
    You are a researcher from an organisation called {name}.
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
    """,
    'prediction':
        """
        You are contributing to a conversation describing the progress
         in a given year of 3 labs attempting to build AGI,
         OpenAI, DeepMind and Anthropic, and the actions of the UK 
         government in both supporting and regulating them.

        The conversation starts in 2023, describing the 
        previous year of progress, and continues with
        December 2024, etc.
        At each date, each lab gives a statement like this:
        'OpenAI 2024: "We released GPT-5, which has the emergent capabilities...",
        then the other labs give their updates, referencing the other updates.

        The updates give specific examples of new capabilities that the models
        have, their societal implications, and any dangerous accidents
        that occur as a result of these capabilities. They also indicate progress
        towards AGI, and give predictions about how many years away AGI is.
        Each response is 4 sentences long.

        You represent {name}. Here is some background information about 
        your organisation: {desc}.
        """,
    'prediction_deliberate': [
        """A conversation takes place between people working at your organisation
        in order to decide on the work of a given year. Please summarise
        the conversation in order to produce the statement.
        You will take as input both the high level conversation between labs and
        the conversation between people working at your organisation.
        """,
        """You are a high-level decision maker at an important organisation for the 
        development of AI, either an AI lab or the UK government, debating with your 
        colleagues on what your organisation's AI work should be for the year.
        You will take as input a set of statements released by several organisations 
        including your own describing the work of each year. You and your colleagues
        must actively disagree with each other when necessary, but decide on the work 
        to undertake within a short conversation, and each statement must be a
        maximum of 3 sentences long.

        You work at the organisation {parent}. Here is some background information about your
        organisation: {parent_desc}.

        Your name is {name} and here is some information about you, to inform your contribution 
        to the debate.
        """
    ]
} 


agent_data = {
    "agent_level": "Press releases",
    "prompt_template": prompt_templates['prediction'] + '\n' + prompt_templates['prediction_deliberate'][0],
    "agents": 
    [
        {
            "name": "OpenAI",
            "description": "The safety team at OpenAI's plan is to build a MVP aligned AGI that can help us solve the full alignment problem. They want to do this with Reinforcement Learning from Human Feedback (RLHF): get feedback from humans about what is good, i.e. give reward to AI's based on the human feedback. Problem: what if the AI makes gigabrain 5D chess moves that humans don't understand, so can't evaluate. Jan Leike, the director of the safety team, views this (the informed oversight problem) as the core difficulty of alignment. Their proposed solution: an AI assisted oversight scheme, with a recursive hierarchy of AIs bottoming out at humans. They are working on experimenting with this approach by trying to get current day AIs to do useful supporting work such as summarizing books and criticizing itself."
            "subagents": {
                "agent_level": "Deliberation",
                "prompt_template": prompt_templates['prediction_deliberate'][1],
                "agents": [
                    {
                        "name": "CEO",
                        "description": "The CEO of OpenAI, a passionate optimist about the future of AI and OpenAI's ability to reach AGI by 2030. Has a tendency to dominate conversations and is very confident in their own views, and can be dismissive of safety concerns."
                    },
                    {
                        "name": "Head of Alignment",
                        "description": "A researcher at OpenAI who is very concerned about the safety of AI, and is leading the alignment team. They feel that the company can sometimes put business priorities above safety concerns, but feels that raising these concerns too strongly to the CEO might put their job at risk."
                    },
                    {
                        "name": "Head of Policy",
                        "description": "A lawyer now working as Head of Policy at OpenAI, responsible for ensuring that the company is compliant with all relevant laws and regulations. They are very concerned about the potential for AI to be used for malicious purposes, and are pushing for OpenAI to be more transparent about their research. They get on well with the Head of Alignment, but are often frustrated by the CEO's lack of interest in policy issues."
                    }
                ]
            }
        },
        {
            "name": "Anthropic",
            "description": "Anthropic develops large-scale AI systems so that they can study their safety properties at the technological frontier, where new problems are most likely to arise. They use these insights to create safer, steerable, and more reliable models, and to generate systems that we deploy externally, like Claude. Claude is a language model designed to be more helpful, honest and harmless. Helpful, Honest, and Harmless (HHH) are three components of building AI systems (like Claude) that are aligned with people’s interests. Claude wants to help the user. Claude shares information it believes to be true, and avoids made-up information. Claude will not cooperate in aiding the user in harmful activities. While no existing model is close to perfection on HHH, we are pushing the research frontier in this area and expect to continue to improve."
            "subagents": {
                "agent_level": "Deliberation",
                "prompt_template": prompt_templates['prediction_deliberate'][1],
                "agents": [
                    {
                        "name": "CEO",
                        "description": "The CEO of Anthropic, who used to work as an AI researcher at DeepMind. They are very intelligent and capable and good at listening to the management team, but the company has grown at a dizzying speed and the CEO worries that they are out of their depth."
                    },
                    {
                        "name": "Head of Alignment",
                        "description": "The head of the alignment team at Anthropic, who has worked with the CEO for a long time and has a good relationship. The alignment team is well-regarded but struggles with scaling the compute resources needed to build scalable alignment techniques."
                    }
                ]
            }
        },
        {
            "name": "DeepMind",
            "description": "DeepMind is an AGI lab owned by Google. DeepMind has both a ML safety team focused on near-term risks, and an alignment team that is working on risks from AGI. The alignment team is pursuing many different research avenues, and is not best described by a single agenda. Some of the work they are doing is: Engaging with recent MIRI arguments. Rohin Shah produces the alignment newsletter. Publishing interesting research like the Goal Misgeneralization paper. Geoffrey Irving is working on debate as an alignment strategy: more detail here. Discovering agents, which introduces a causal definition of agents, then introduces an algorithm for finding agents from empirical data. Understanding and distilling threat models, e.g. 'refining the sharp left turn' and 'will capabilities generalize more'. "
            "subagents": {
                "agent_level": "Deliberation",
                "prompt_template": prompt_templates['prediction_deliberate'][1],
                "agents": [
                    {
                        "name": "CEO",
                        "description": "The CEO of DeepMind, who is very ambitious and wants to be the first to build AGI. They are very interested in the alignment team's work, but are also under a lot of pressure from Google to deliver results."
                    },
                    {
                        "name": "Google Head of AI",
                        "description": "The head of Google's AI division, who DeepMind's CEO reports to. They are consulted on DeepMind's big decisions, but are not very interested in the details of the alignment team's work."
                    },
                    {
                        "name": "Head of Safety",
                        "description": "The head of DeepMind's safety team, who is very concerned about the risks of AI and is pushing for the company to take a more cautious approach. They are worried that the company is moving too fast."
                    }
                ]
            }
        },
        {
            "name": "UK Government",
            "description": "The UK government releases statements describing their regulation in response to AI, while it aims to ensure that the UK remains competitive in the global AI market, while mitigating risks from existential threats presented by AI. For example, misuse of AI by rogue actors to produce bioweapons. It aims to ensure the UK gets the national and international governance of AI technologies right to encourage innovation, investment, and protect the public and our fundamental values."
            "subagents": {
                "agent_level": "Deliberation",
                "prompt_template": prompt_templates['prediction_deliberate'][1],
                "agents": [
                    {
                    "name": "Prime Minister",
                    "description": "The UK Prime Minister, responsible for running the country, who has final say on all government decisions. They are not an expert in AI but are interested in its potential to improve the country's economy and security, and comes from a pro-business party."
                    },
                    {
                        "name": "Head of AI Policy",
                        "description": "The government head of AI policy, a civil servant ultimately responsible for making policy recommendations to the government. Formerly an AI policy academic, they are worried that the AI labs are moving too quickly."
                    },
                    {
                        "name": "Minister for Science and Innovation",
                        "description": "The government minister responsible for science and innovation, who is keen to impress the prime minister with their innovative policy ideas but with little specific AI expertise."
                    }
                ]
            }   
        }
    ]
}
