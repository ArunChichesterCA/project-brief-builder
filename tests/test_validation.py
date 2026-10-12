import unittest

from validation import validate_brief


class TestValidation(unittest.TestCase):
    def test_complete_brief_has_no_problems(self):
        data = {
            "title": "Room booking helper",
            "problem": "Room availability is difficult to check.",
            "users": "Office staff",
            "outcome": "Staff can identify an available room.",
            "essential_features": "Show rooms",
            "out_of_scope": "No live calendar connection",
            "constraints": "Fictional data only",
            "acceptance_criteria": "Three sample rooms appear",
        }
        self.assertEqual(validate_brief(data), [])

    def test_missing_title_is_reported(self):
        self.assertIn("Project title is required.", validate_brief({}))

    def test_spaces_do_not_count_as_content(self):
        messages = validate_brief({"title": "   "})
        self.assertIn("Project title is required.", messages)


if __name__ == "__main__":
    unittest.main()
