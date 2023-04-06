# %%
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

import os
from dotenv import load_dotenv
load_dotenv()


# %%
OPENAI_API_KEY = os.getenv('OPENAI_API_TOKEN')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# %%
# declare the chat
chat = ChatOpenAI(temperature=0)

# %%
# basic use of chat with human messages
chat([HumanMessage(content="Translate this sentence from English to Chinese. I love programming.")])

# %%
# compex use utilizing multiple prompts & system messages
messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming.")
]
chat(messages)

# %%
# using prompts
template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
chat(chat_prompt.format_prompt(input_language="English",
     output_language="French", text="I love programming.").to_messages())

# %%
# using chat to create a chain
chain = LLMChain(llm=chat, prompt=chat_prompt)
chain.run(input_language="English", output_language="French",
          text="I love programming.")

# %%
