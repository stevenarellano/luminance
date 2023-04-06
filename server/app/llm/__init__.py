# %%
from langchain.llms import OpenAI
from langchain import LLMChain, PromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

# %%
question = "Which NFL team won the Super Bowl in the 2010 season?"

# %%
OPENAI_API_KEY = os.getenv('OPENAI_API_TOKEN')


davinci = OpenAI(model_name='text-davinci-003', openai_api_key=OPENAI_API_KEY)

llm_chain = LLMChain(
    prompt=prompt,
    llm=davinci
)

# %%
print(llm_chain.run(question=question))

# %%
