# %%
from langchain.llms.loading import load_llm
from langchain.llms import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()


# %%
OPENAI_API_KEY = os.getenv('OPENAI_API_TOKEN')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# %%
# generate text (most basic functionality)
llm = OpenAI(model_name='text-curie-001', openai_api_key=OPENAI_API_KEY)
llm("tell me a joke")


# %%
# generate (input a list)
llm.generate(["tell me a joke", "tell me another joke"])

# %%
# checking the number of tokens
num_tokens = llm.get_num_tokens("tell me a joke")
print(f"Number of tokens: {num_tokens}")

# %%
loaded_llm = load_llm("llm.json")

# %%
