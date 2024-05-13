"""Module to test facts API endpoint."""

import pytest

FACTS_ENDPOINT = "/facts"

import pytest


@pytest.mark.parametrize("limit", [1, 25, 50, 100, 150, 200, 1000])
def test_number_of_facts_within_specified_limit(http_get_request, limit):
    """
    Test the number of facts returned are within the specified limit.

    Parameters:
    - http_get_request: Fixture to make requests to the API.
    - limit: Int specifying the maximum number of facts to retrieve.
    """
    response = http_get_request(endpoint=FACTS_ENDPOINT, params={"max_length": 100, "limit": limit})

    assert response.status_code == 200, f"Expected HTTP status code 200, but received {response.status_code}"

    response_json = response.json()
    assert len(response_json["data"]) <= limit, "Returned number of facts not within the specified limit"
