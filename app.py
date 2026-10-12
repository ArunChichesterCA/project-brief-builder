import streamlit as st

from brief_generator import generate_brief
from validation import validate_brief


st.set_page_config(page_title="Project Brief Builder", page_icon="🧭", layout="wide")
st.title("Project Brief Builder")
st.write("Turn a rough project idea into a clear, structured starting brief.")

with st.form("brief_form"):
    title = st.text_input("Project title")
    problem = st.text_area("What problem should the project solve?")
    users = st.text_area("Who will use or benefit from it?")
    outcome = st.text_area("What should be different when the project succeeds?")
    essential_features = st.text_area("Essential features (one per line)")
    optional_features = st.text_area("Optional features (one per line)")
    out_of_scope = st.text_area("Out of scope (one per line)")
    constraints = st.text_area("Data, security or other constraints (one per line)")
    acceptance_criteria = st.text_area("Acceptance criteria (one per line)")
    submitted = st.form_submit_button("Build project brief")

if submitted:
    brief_data = {
        "title": title,
        "problem": problem,
        "users": users,
        "outcome": outcome,
        "essential_features": essential_features,
        "optional_features": optional_features,
        "out_of_scope": out_of_scope,
        "constraints": constraints,
        "acceptance_criteria": acceptance_criteria,
    }

    problems = validate_brief(brief_data)
    if problems:
        st.error("Please improve the brief before downloading it.")
        for problem_message in problems:
            st.write(f"- {problem_message}")
    else:
        brief_text = generate_brief(brief_data)
        st.success("Your project brief is ready.")
        st.markdown(brief_text)
        st.download_button(
            "Download Markdown brief",
            data=brief_text,
            file_name="project_brief.md",
            mime="text/markdown",
        )
