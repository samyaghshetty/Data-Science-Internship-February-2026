from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.extract_prompt import extract_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=30,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

extract_chain = extract_prompt | llm