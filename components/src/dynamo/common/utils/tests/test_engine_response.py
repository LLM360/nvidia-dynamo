#  SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#  SPDX-License-Identifier: Apache-2.0

import pytest

from dynamo.common.utils.engine_response import normalize_finish_reason

pytestmark = [pytest.mark.unit, pytest.mark.pre_merge]


def test_normalize_finish_reason_wraps_bare_error():
    assert normalize_finish_reason("error") == {"error": "backend error"}


def test_normalize_finish_reason_extracts_error_payload():
    assert normalize_finish_reason("error: timeout") == {"error": "timeout"}


def test_normalize_finish_reason_preserves_non_error_values():
    assert normalize_finish_reason("stop") == "stop"
