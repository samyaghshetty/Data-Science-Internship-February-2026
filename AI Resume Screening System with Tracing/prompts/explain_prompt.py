from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match_data"],
    template="""
Explain in 1-2 lines why this score was given.

Score: {score}

Data:
{match_data}
"""
)