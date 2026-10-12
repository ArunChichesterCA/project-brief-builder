REQUIRED_FIELDS = {
    "title": "Project title",
    "problem": "Problem to solve",
    "users": "Intended users",
    "outcome": "Desired outcome",
    "essential_features": "Essential features",
    "out_of_scope": "Out of scope",
    "constraints": "Constraints",
    "acceptance_criteria": "Acceptance criteria",
}


def validate_brief(brief_data):
    """Return a list of clear validation messages."""
    problems = []
    for field, label in REQUIRED_FIELDS.items():
        if not brief_data.get(field, "").strip():
            problems.append(f"{label} is required.")
    return problems
