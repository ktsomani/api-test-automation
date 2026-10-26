import os

import pytest

RESULTS = []


def pytest_runtest_logreport(report):
    if report.when == "call":
        RESULTS.append((report.nodeid, report.outcome, report.longrepr))


def pytest_sessionfinish(session, exitstatus):
    os.makedirs("results", exist_ok=True)
    passed = sum(1 for _, o, _ in RESULTS if o == "passed")
    failed = sum(1 for _, o, _ in RESULTS if o == "failed")
    lines = [
        "# Test Summary",
        "",
        f"- Passed: {passed}",
        f"- Failed: {failed}",
        "",
        "## Failures",
    ]
    for nodeid, outcome, longrepr in RESULTS:
        if outcome == "failed":
            lines.append(f"- {nodeid}: see junit output for details")
    with open("results/SUMMARY.md", "w") as f:
        f.write("\n".join(lines) + "\n")
