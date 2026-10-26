# API Test Automation

Automated tests for the public JSONPlaceholder REST API using pytest and
requests, with a defect log that records each finding in a reviewable format.

## Tech

Python, pytest, requests, JUnit XML output, Markdown defect reporting.

## Run

```bash
pip install -r requirements.txt
pytest -v --junitxml=results/junit.xml
```

After each run, `results/SUMMARY.md` lists pass/fail counts and failing tests.

## Structure

- `tests/test_users.py`: list, fetch, create, and not-found cases for users
- `tests/test_posts.py`: list, fetch, filter, update, and edge cases for posts
- `tests/test_comments.py`: comments per post and field validation
- `conftest.py`: writes the summary report
- `config.py`: base URL and timeout
- `DEFECTS.md`: defect log (ID, severity, steps, expected vs actual)

## Coverage

| Area     | Happy path | Edge cases | Error handling |
|----------|------------|------------|----------------|
| Users    | yes        | yes        | yes            |
| Posts    | yes        | yes        | yes            |
| Comments | yes        | yes        | partial        |

## Findings

Two issues are logged in `DEFECTS.md`: an empty post title is accepted, and a
non-numeric user ID returns 404 instead of 400.

## Limitations and next steps

- JSONPlaceholder is a fake API that does not persist writes, so create and
  update tests check the response only.
- Next: add JSON Schema validation and a Postman/Newman collection.
