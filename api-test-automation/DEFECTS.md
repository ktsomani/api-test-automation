# Defect Log

Format per entry: ID, title, severity, steps to reproduce, expected vs actual.

## DEF-001: Empty post title accepted
- **Severity**: Minor
- **Steps**: POST /posts with `{"title": "", "body": "x", "userId": 1}`
- **Expected**: 400 Bad Request, title is required
- **Actual**: 201 Created
- **Note**: Recorded as a finding. `tests/test_posts.py::test_empty_title_is_accepted_documented_defect` documents current behaviour.

## DEF-002: Non-numeric user ID returns 404 instead of 400
- **Severity**: Minor
- **Steps**: GET /users/abc
- **Expected**: 400 Bad Request (malformed ID)
- **Actual**: 404 Not Found
