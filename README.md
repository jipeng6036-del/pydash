# Right-reduction index validation

Repository: dgilland/pydash. Baseline `ef6a6427e488e29e827e0e0819f2630ad3ff4cdc`, candidate `5674ec55d429ade516688fe696688d588b246aa9`.

`reduce_right` previously reversed the values and then enumerated them from zero. A callback using the original row index therefore returned incorrect results. The candidate reverses original key/value pairs; rightward intermediate reductions inherit the correction. No external production incident or independent human review is claimed.

## Results

- New regressions on Python 3.13.1: baseline 6 fail; candidate 6 pass (lists, tuples, iterators; explicit and implicit accumulators).
- Configured Windows unit/doctest profile: baseline 2880 pass / candidate 2886 pass, both 100% coverage. The optional mypy-fixture suite is excluded exactly as official `inv test` does; full ordinary mypy checks pass separately.
- Official Linux `tox -e py310`, `py311`, `py312`, `py313`, `py314` each pass: build, strict Sphinx docs, full Ruff format/lint, mypy, generated chaining type byte comparison, and 2886 unit/doctests with 100% coverage.
- Each tox-installed package passes the CSV consumer in `pydash-consumer.py`. Windows original vs candidate consumer also recorded. Expected reverse row positions are 2,1,0 and weighted totals 90,130,140; baseline totals are 30,70,100.
- All 78 baseline/candidate exported Git blobs and modes were independently checked. Canonical export used `git -c core.autocrlf=false archive <SHA>`; the earlier CRLF export was rejected and none of its results count here.

## Reproduce

Check out the candidate and run `tox` with Python 3.10 through 3.14 installed, or each named tox environment in its matching Python image. The exact commands/images/versions are in the matrix JSON and logs. The default CI profile intentionally excludes `tests/pytest_mypy_testing`; it runs standalone mypy instead. Run `pydash-consumer.py` against the installed package. To reproduce the six regression failures, keep final `tests/test_collections.py` and use the exact baseline production source.

Published logs remove ANSI sequences and normalize local workspace/home paths; results and commands otherwise remain unchanged. Raw originals and superseded attempts are retained locally. No paid service, remote inference, or personal credentials were used.
