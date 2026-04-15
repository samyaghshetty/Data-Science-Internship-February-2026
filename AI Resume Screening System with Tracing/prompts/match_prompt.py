from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job"],
    template="""
Compare resume with job.

Return:
Matching Skills:
Missing Skills:

Resume:
{resume_data}

Job:
{job}
"""
)