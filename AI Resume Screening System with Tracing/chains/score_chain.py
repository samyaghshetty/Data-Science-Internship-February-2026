from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts.score_prompt import score_prompt

pipe = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=10,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

score_chain = score_prompt | llm