# Alignment research simulator!

A small project that hopes to at least be entertaining, but points to a potentially promising future research project.
If we can simulate the process of AI research, with an AI model assuming the personas of real researchers or organisations,
it could point to potential future developments or points of (dis)agreement between research agendas.

Following the architecture described [here](https://arxiv.org/pdf/2304.03442v1.pdf) this idea could be extended to simulate a whole population of AI researchers and their actions.

## Findings
- GPT 3.5 produced endlessly recurring, endlessly agreeing conversations between OpenAI and Anthropic about the importance of collaboration on AI research. The conversation was the same even when explicitly told to try and disagree. When given the same prompt, GPT 4 produced a much more coherent debate where the respondents actively disagreed.

- The first run using GPT 4, and just including OpenAI, DeepMind and Anthropic, thought that AGI will come in 2031, and be developed at the same time by all three labs. It also predicted that the labs will collaborate heavily with each other, to the extent of using each others' models to underpin their own. From early in the run, the labs predict around 2030-32 to reach AGI, consistently give this estimate every year, and are eventually correct in this estimate. From there, AGI revolutionises society with no apparent downsides, though the labs continuously work on safety precautions.

- The next run asked the labs to give examples of dangerous accidents caused by these models and introduced the UK Government as a regulator. This creates a much more winding and cautious path to AGI, full of unexpected side-effects. These side-effects make the labs extend their timelines each year, ending with predictions in the late 2030s (the era of GPT 17) of AGI still being 20 years away. The government's response is toothless in this run. It offers commentary and calls for regulation without realising that it can make it.