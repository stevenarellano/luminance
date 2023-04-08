# %%
from langchain.llms import OpenAI
from langchain import LLMChain

from .llm_config import OPENAI_API_KEY


def create_llm() -> OpenAI:
    return OpenAI(model_name='text-curie-001', openai_api_key=OPENAI_API_KEY)
