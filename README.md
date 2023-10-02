# Converse

A general-purpose framework for simulating conversations between agents, powered by GPT-4.

This approach uses agents mapped to separate objects in code, each with individual system prompts and contributing to a conversation, rather than having a single prompt to predict the whole conversation. This allows for more complex conversations, with each agent able to hold its own context that is not visible to the others. This might include its own deliberative process, simulated through a separate, nested conversation.

Use cases:

## AI research simulator!

A small project that hopes to at least be entertaining, but points to a potentially promising future research project. If we can simulate the process of AI research, with an AI model assuming the personas of real researchers or organisations, it could point to potential future developments and research agendas. It can allow us to run versions of the future with different parameters: turning dials of the amount of regulation, number of AI labs, competition from China, etc, to give us an idea of what the future might hold and where to focus our efforts.

Following the architecture described [here](https://arxiv.org/pdf/2304.03442v1.pdf) this idea could be extended to simulate a whole population of AI researchers and their actions.


### Debate
---
A debate between OpenAI, DeepMind and Anthropic on the relative merits of their AI alignment research agendas.

A two-way debate between OpenAI and Anthropic on GPT 3.5 produced an [endlessly recurring, endlessly agreeing conversation](converse/conversations/ai-debate/ai-lab-debate-gpt3.5) about the importance of collaboration on AI research, even when explicitly told to disagree.

When given the same prompt, and introducing DeepMind, GPT 4 produced a [much more coherent debate](converse/conversations/ai-debate/ai-lab-debate-gpt4) where the respondents actively disagreed.


### Prediction (on GPT 4)

---
Aiming to simulate the annual progress of AI research, with each agent giving a statement on their progress so far, including specific model capabilities, safety incidents and AGI timeline estimates.

[A simulation involving OpenAI, DeepMind and Anthropic](converse/conversations/ai-predictions/agi-6-monthly) predicted that AGI would arrive in 2031, and be developed at the same time by all three labs:

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
