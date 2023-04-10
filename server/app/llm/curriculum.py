from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

from .create_llm import create_llm

from pydantic import BaseModel, Field, validator
from langchain.output_parsers import PydanticOutputParser
from typing import List, Dict, Union, TypeAlias

import json

CurriculumItem: TypeAlias = Dict[str, Union[str, List[str]]]
CurriculumList: TypeAlias = List[CurriculumItem]


class Curriculum(BaseModel):
    curriculum: CurriculumList = Field(
        description="curriculum for the degree where the dict has the keys 'title' and 'topics'")

    @validator('curriculum')
    def curriculum_validator(cls, v):
        for item in v:
            if not isinstance(item, dict):
                raise ValueError("curriculum must be a list of dicts")
            if not "title" in item:
                raise ValueError("curriculum must have a title")
            if not "topics" in item:
                raise ValueError("curriculum must have topics")
        return v


template = """
write me a curriculum for a {topic} degree with everthing i need to know as a phd level, 
break it up into themes. respond in under 800 characters no matter what.

{format_instructions}.
"""

parser = PydanticOutputParser(pydantic_object=Curriculum)
prompt = PromptTemplate(
    template=template,
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


def get_curriculum(topic: str) -> CurriculumList:
    _input = prompt.format_prompt(topic=topic)
    llm = create_llm()
    output = llm(_input.to_string())
    response_obj = parser.parse(output)
    return response_obj.curriculum


if __name__ == "__main__":
    topic = "computer science"
    result = get_curriculum(topic)
    print(json.dumps(result, indent=4))
