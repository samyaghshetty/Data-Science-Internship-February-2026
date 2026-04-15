from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Give a score from 0 to 100.

ONLY return number.
NO explanation.

Example:
80

Data:
{match_data}
"""
)