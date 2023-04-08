# %%

from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from examples import example_dict

template = """
write me a curriculum for a {topic} degree with everything i need to know as a phd level, don't break it up into years, but into themes including any needed foundations.
"""

sample_prompts = "write me a curriculum for a computer science degree with everthing i need to know as a phd level, break it up into themes. respond in only json, nothing else; here's an example:"

example_template = "Input: {input}\nOutput: {output}"

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_template
)

prompt = FewShotPromptTemplate(
    examples=example_dict,
    example_prompt=example_prompt,
    suffix=template,
    input_variables=["topic"],
)

print(prompt.format(topic="biology"))
