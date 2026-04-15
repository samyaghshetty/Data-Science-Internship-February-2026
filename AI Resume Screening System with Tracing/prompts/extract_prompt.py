from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract skills, experience, and tools.

Return format:
Skills:
Experience:
Tools:

Resume:
{resume}
"""
)