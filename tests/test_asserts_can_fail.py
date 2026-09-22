"""Guard against the untested test.

An assert that cannot fail is not a test. `all(x > 0 for x in [])` is vacuously true, and
a lesson built on one teaches nothing. Every notebook assertion should have a counterpart
here that sabotages the thing it guards and confirms the assertion fails.
"""

import pytest


@pytest.mark.xfail(reason="TODO: sabotage the guarded code and confirm this fails")
def test_segmentation_assert_detects_merged_cells():
    raise NotImplementedError


@pytest.mark.xfail(reason="TODO: sabotage the guarded code and confirm this fails")
def test_null_tissue_assert_detects_miscalibrated_test():
    raise NotImplementedError
