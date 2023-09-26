
persona_data = [
    {
        "name": "OpenAI",
        "description": "The safety team at OpenAI's plan is to build a MVP aligned AGI that can help us solve the full alignment problem. They want to do this with Reinforcement Learning from Human Feedback (RLHF): get feedback from humans about what is good, i.e. give reward to AI's based on the human feedback. Problem: what if the AI makes gigabrain 5D chess moves that humans don't understand, so can't evaluate. Jan Leike, the director of the safety team, views this (the informed oversight problem) as the core difficulty of alignment. Their proposed solution: an AI assisted oversight scheme, with a recursive hierarchy of AIs bottoming out at humans. They are working on experimenting with this approach by trying to get current day AIs to do useful supporting work such as summarizing books and criticizing itself."
    },
    {
        "name": "Anthropic",
        "description": "Anthropic develops large-scale AI systems so that they can study their safety properties at the technological frontier, where new problems are most likely to arise. They use these insights to create safer, steerable, and more reliable models, and to generate systems that we deploy externally, like Claude. Claude is a language model designed to be more helpful, honest and harmless. Helpful, Honest, and Harmless (HHH) are three components of building AI systems (like Claude) that are aligned with people’s interests. Claude wants to help the user. Claude shares information it believes to be true, and avoids made-up information. Claude will not cooperate in aiding the user in harmful activities. While no existing model is close to perfection on HHH, we are pushing the research frontier in this area and expect to continue to improve. "
    },
    {
        "name": "DeepMind",
        "description": "DeepMind is an AGI lab owned by Google. DeepMind has both a ML safety team focused on near-term risks, and an alignment team that is working on risks from AGI. The alignment team is pursuing many different research avenues, and is not best described by a single agenda. Some of the work they are doing is: Engaging with recent MIRI arguments. Rohin Shah produces the alignment newsletter. Publishing interesting research like the Goal Misgeneralization paper. Geoffrey Irving is working on debate as an alignment strategy: more detail here. Discovering agents, which introduces a causal definition of agents, then introduces an algorithm for finding agents from empirical data. Understanding and distilling threat models, e.g. 'refining the sharp left turn' and 'will capabilities generalize more'. "
    },
    {
        "name": "UK Government",
        "description": "The UK government aims to ensure that the UK remains competitive in the global AI market, while mitigating risks from existential threats presented by AI. For example, misuse of AI by rogue actors to produce bioweapons. It aims to ensure the UK gets the national and international governance of AI technologies right to encourage innovation, investment, and protect the public and our fundamental values."
    }
]

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
    'prediction': """
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
    """
} 
