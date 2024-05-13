"""Module to test random fact API endpoint."""

import pytest

FACT_ENDPOINT = "/fact"


def test_random_fact_length_matches_returned_length(http_get_request):
    """
    Test returned random fact length matches the returned length.

    Parameters:
    - http_get_request: Fixture to make requests to the API.
    """
    response = http_get_request(endpoint=FACT_ENDPOINT)

    assert response.status_code == 200, "Expected HTTP status code 200"
    response_data = response.json()
    assert len(response_data["fact"]) == response_data["length"], "Returned fact length does not match returned length"


@pytest.mark.parametrize("max_length", [28, 50, 100, 1000])
def test_random_fact_length_is_within_max_length(http_get_request, max_length):
    """
    Test that random fact has a length within the specified maximum length.

    Parameters:
    - http_get_request: Fixture to make requests to the API.
    - max_length: Int specifying the maximum fact length.
    """
    response = http_get_request(endpoint=FACT_ENDPOINT, params={"max_length": max_length})

    assert response.status_code == 200, "Expected HTTP status code 200"
    response_data = response.json()
    assert len(response_data["fact"]) <= max_length, "Returned fact exceeds specified maximum length"


@pytest.mark.parametrize("max_length", [1, 0, -1])
def test_generate_random_facts_with_invalid_max_length(http_get_request, max_length):
    """
    Test generating random fact with max length set to zero.

    Parameters:
    - http_get_request: Fixture to make requests to the API.
    - max_length: Int specifying the maximum fact length.
    """
    response = http_get_request(endpoint=FACT_ENDPOINT, params={"max_length": max_length})

    assert response.status_code == 200, "Expected HTTP status code 200"
    assert response.json() == {}, "Expected empty response for invalid max length"
