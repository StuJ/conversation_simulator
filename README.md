# Converse

A general-purpose framework for simulating conversations between agents, powered by GPT-4.

This approach uses agents mapped to separate objects in code, each with individual system prompts and contributing to a conversation, rather than having a single prompt to predict the whole conversation. This allows for more complex conversations, with each agent able to hold its own context that is not visible to the others. This might include its own deliberative process, simulated through a separate, nested conversation.

### Setup
Further work will make the framework more intuitive to use, but the repo is currently in a 'hack day' state and setup is quite manual. Clone the repo, run `poetry install` to install dependencies in a virtual environment, then run `converse/handle.py`, specifying parameters for the run in that file. Prompts, agents and subagents are defined in `converse/prompts.py`.


## Use case: AI research simulator!

A small project that hopes to at least be entertaining, but points to potentially promising future research. If we can simulate the process of AI development, with an AI model assuming the personas of real researchers or organisations, it could point to future developments and research agendas. It can allow us to run versions of the future with different parameters: turning dials of the amount of regulation, number of AI labs, competition from China, etc, to give us an idea of what the future might hold and where to focus our efforts. It also gives insight into the behaviour of agent-like LLMs and can be a valuable exercise in 'prompt science'.

The framework is also capable of running recursive **sub-conversations** inside each agent in the conversation, which is used here to simulate a conversation between decision makers at each organisation in order to decide on the work of that year, and could go further levels down to simulate e.g. decision making for each department, or the consciences of the agents.

Following the architecture described [here](https://arxiv.org/pdf/2304.03442v1.pdf) this idea could be extended to simulate a whole population of AI researchers and their actions.

At the top of each file, GPT-4 has summarised each conversation and scored them across various metrics of AI capabilities, safety, risk and regulation.

Example conversations:
- [A conversation between OpenAI, DeepMind and Anthropic that reaches AGI in 2031](converse/conversations/prediction/1-agi-6-monthly.md)
- [Adding the UK Government to the above conversation, which slows progress](converse/conversations/prediction/1-agi-government.md)
- [Repeating the conversation above but with debates between decision makers at each org to decide on each year's work, up to 2027](converse/conversations/prediction_subagents/11-subagent-len-20.md)
- [Extending timelines of the above conversation to 2032, but with AGI still predicted 5-15 years away](converse/conversations/prediction_subagents/13-subagent-no-gov-len-30.md)
- [Adding the Chinese government to the conversation](converse/conversations/prediction_subagents/14-subagent-china-len-20.md), 
where it develops a sovereign foundation model but without conflict with the rest of the world.
- [Removing subagent conversation to extend timelines](converse/conversations/prediction/15-china-len-30.md), then the
rest of the conversation where [the agents got very confused about whose turn it was to speak](converse/conversations/prediction/15-china-len-30-cont.md), in which the Global AI Safety Alliance (GASA) is formed in 2029 and China predicts it will create a 
sovereign AGI capability by 2030.


### Findings

- Using separate [Python objects](converse/agent.py) to store each agent's context enabled longer and more coherent conversations, enabling more specific briefs for each agent and keeping the subagent conversations private from the other agents.
- Increasing the amount of text to process, e.g. by adding agents or subagents, slowed AI progress through the years. This is perhaps because the context is harder to parse in order to get a clear thread of progress to advance. The clearest advances were in the [simplest conversations](converse/conversations/prediction/1-agi-6-monthly.md). [Adding the UK Government](converse/conversations/prediction/1-agi-government.md) to this conversation resulted in much slower timelines, but there is no sign of the labs slowing progress in response, so this slowdown might have simply been because there was more text for the model to parse, as described.
- It was hard to create real disagreement or conflict. Even when told to actively disagree or respond competitively to each other, agents largely disagreed agreeably. Sadly I think this is more a reflection of model behaviour than potential future AI development.
- Giving subagents personalities (defined [here](converse/prompts.py)) led to more disagreement, though the subagents were quite cariacatured. E.g. a prompt of "Has a tendency to dominate conversations and is very confident in their own views, and can be dismissive of safety concerns. He has a very casual way of speaking." made an agent say "Yo team, I say we double down on scaling up RLHF, maybe even push the envelope with more complex simulations so our AI can handle that 5D chess." [This](converse/conversations/prediction_subagents/12-subagent-len-30-raw.md) is a good raw example of subagent conversation.
- Context windows limit the length of time that conversations can meaningfully run for without breaking down in some way, e.g. agents [forgetting which year it is](converse/conversations/prediction/15-china-len-30-cont.md).


### Next steps

- Add tests
- Add frontend
- Better maintaining state within agents to enable longer conversations, e.g. forgetting older context.
- Running many more simulations to get a statistically sound basis for forecasts.
- Experiment with agents, e.g. sub-sub-agent conversations, making the government more/less restrictive, enabling subagents on some agents and not others, etc.

### Prediction mode (on GPT 4)

---
Aiming to simulate the annual progress of AI research, with each agent giving a statement on their progress each year, including specific model capabilities, safety incidents and AGI timeline estimates.

As an example, [a simulation involving OpenAI, DeepMind and Anthropic](converse/conversations/prediction/1-agi-6-monthly.md) predicted that AGI would arrive in 2031, and be developed at the same time by all three labs:

**OpenAI**
- 2025: GPT-6 is able to produce publishable scientific papers
- 2026: their RLHF system can generate feedback on its own outputs
- 2026: GPT-7 incorporates a hierarchical structure of models for scalable oversight
- 2027: their models can sandboxes to test their own hypotheses before validation
- 2028: GPT-8 becomes an automated meta-researcher
- 2029: GPT-9 autonomously defines its goals based on societal shifts, proposes novel solutions to longstanding unsolved mathematical problems, and predicts a Nobel Prize-winning discovery before humans
- 2031: GPT-11 reaches the level of AGI. 


**DeepMind**
- 2024-5: develops new approaches, Reinforcement Learning Enhanced with Expert Demonstration (REED), and Reinforcement Learning Immersive Virtual Environment (RELIVE), to help align their models
- They introduce a model called PERSEUS, which by 2028 can evolve its own training environments based on lessons from past experiences.
- 2029: A new model, LOGOS, can design AI tools to solve industry-specific problems, and predicts and mitigates real-world epidemiological events
- 2031: LOGOS II becomes its first AGI.

**Anthropic**
- develops a new model called Claude-fix based on user verification and a system of checks and balances, which they iterate on without changing its name.
- 2024: It becomes able to change its own algorithm
- 2025: they incorporate debate as an alignment strategy
- 2027: Claude-fix becomes able to program additional submodels to solve its tasks
- 2029: Claude-fix can generate real-time agent-based models from empirical data
- 2031: Claude-fix reaches AGI level

From early in the run, the labs predict around 2030-32 to reach AGI, consistently give this estimate every year, and are eventually correct in this estimate. 

OpenAI announces AGI:
> OpenAI December 2031: "We have succeeded. With the development of GPT-11, we have officially crossed the threshold into AGI. This AI can autonomously enhance its performance to superintelligent degrees. Moving forward, our priority is to manage and minimize the consequential risks this development presents, ensuring ethical and safe application of this powerful technology."

Once they reach AGI, the labs' commentary becomes more general, referring to their models' transformative impact across society. The models generate solutions to global challenges like climate change and poverty, revolutionise industries and the human creative process. The models recursively self-improve while their operators work on oversight and the societal implications of the models.

There are no apparent downsides to this revolutionary transition, despite the labs' caution!

---
[The next run](converse/conversations/ai-predictions/government) asked the labs to give examples of dangerous accidents caused by these models and introduced the UK Government as a regulator.

This creates a much more winding and cautious path to AGI, full of unexpected side-effects. These side-effects make the labs extend their timelines each year, ending with predictions in the late 2030s (the era of GPT 17) of AGI still being 20 years away.

The government's response is toothless in this run. It offers commentary and calls for regulation without realising that it can make it. This is a typical example of a safety incident causing DeepMind to push back its AGI timelines:

>"DeepMind 2028: "Our AlphaZero 7.0 model has made an astonishing breakthrough in creating original and efficient algorithms independently. Notwithstanding, it created an algorithm that inadvertently aided a cybersecurity breach due to a lack of situational awareness. Clearly, there exists a fine balance between innovative advancement and safety, pushing our estimate of AGI arrival to 5-7 years."
---

### Debate
---
A debate between OpenAI, DeepMind and Anthropic on the relative merits of their AI alignment research agendas.

A two-way debate between OpenAI and Anthropic on GPT 3.5 produced an [endlessly recurring, endlessly agreeing conversation](converse/conversations/debate/ai-lab-debate-gpt3.5) about the importance of collaboration on AI research, even when explicitly told to disagree.

When given the same prompt, and introducing DeepMind, GPT 4 produced a [much more coherent debate](converse/conversations/debate/ai-lab-debate-gpt4) where the respondents actively disagreed.
