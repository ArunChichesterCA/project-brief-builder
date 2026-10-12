import unittest

from brief_generator import as_bullets, generate_brief


class TestBriefGenerator(unittest.TestCase):
    def test_lines_become_bullets(self):
        self.assertEqual(as_bullets("Search\nFilter"), "- Search\n- Filter")

    def test_empty_optional_section_is_clear(self):
        self.assertEqual(as_bullets(""), "- None supplied")

    def test_generated_brief_contains_title(self):
        data = {
            "title": "Test project",
            "problem": "A problem",
            "users": "Test users",
            "outcome": "A useful outcome",
            "essential_features": "One feature",
            "optional_features": "",
            "out_of_scope": "No live systems",
            "constraints": "Fictional data only",
            "acceptance_criteria": "The feature works",
        }
        self.assertTrue(generate_brief(data).startswith("# Test project"))


if __name__ == "__main__":
    unittest.main()
