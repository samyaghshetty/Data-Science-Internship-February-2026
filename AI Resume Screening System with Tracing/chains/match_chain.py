from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.match_prompt import match_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=30,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

match_chain = match_prompt | llm