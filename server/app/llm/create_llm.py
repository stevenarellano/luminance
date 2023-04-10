# %%
from langchain.llms import OpenAI
from langchain import LLMChain

from .llm_config import OPENAI_API_KEY

model_0 = 'text-davinci-003'
model_1 = 'text-curie-001'


def create_llm() -> OpenAI:
    return OpenAI(model_name=model_0, openai_api_key=OPENAI_API_KEY)
