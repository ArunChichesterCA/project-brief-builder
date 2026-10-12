def as_bullets(text):
    """Turn non-empty lines into Markdown bullet points."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "- None supplied"
    return "\n".join(f"- {line}" for line in lines)


def generate_brief(data):
    """Create a complete Markdown project brief from validated form data."""
    return f"""# {data['title'].strip()}

## Problem to solve

{data['problem'].strip()}

## Intended users

{data['users'].strip()}

## Desired outcome

{data['outcome'].strip()}

## Essential features

{as_bullets(data['essential_features'])}

## Optional features

{as_bullets(data.get('optional_features', ''))}

## Out of scope

{as_bullets(data['out_of_scope'])}

## Constraints

{as_bullets(data['constraints'])}

## Acceptance criteria

{as_bullets(data['acceptance_criteria'])}

## Handover checklist

- The finished work has been demonstrated.
- Tests and known limitations have been documented.
- Setup and usage instructions have been written.
- No personal data, passwords or secret keys are included.
"""
