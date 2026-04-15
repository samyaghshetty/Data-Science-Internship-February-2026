from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain
import re

def run_pipeline(resume, job):

    # Limit input size
    resume = resume[:500]
    job = job[:200]

    # Step 1: Extract
    extracted = extract_chain.invoke({"resume": resume})
    extracted = extracted[:300]

    # Step 2: Match
    matched = match_chain.invoke({
        "resume_data": extracted,
        "job": job
    })
    matched = matched[:300]

    # Step 3: Score
    score_raw = score_chain.invoke({
        "match_data": matched
    }).strip()

    # Extract only number
    match = re.search(r"\d+", score_raw)
    score = match.group() if match else "0"

    # Step 4: Explain
    explanation = explain_chain.invoke({
        "score": score,
        "match_data": matched[:200]
    }).strip()

    return score, explanation


if __name__ == "__main__":

    job_description = """
    Data Scientist role requiring:
    Python, Machine Learning, NLP, SQL, Pandas, NumPy
    """

    for file in ["strong.txt", "average.txt", "weak.txt"]:

        print(f"\n--- Evaluating {file} ---")

        with open(f"resumes/{file}") as f:
            resume = f.read()

        score, explanation = run_pipeline(resume, job_description)

        print("Score:", score)
        print("Explanation:", explanation)