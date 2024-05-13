"""Module to provide fixtures for testing API endpoints."""

import pytest
import requests
from typing import Callable, Optional

from config import settings


@pytest.fixture
def base_url() -> str:
    """
    Fixture to provide the base URL of the API.

    Returns:
        str: The base URL.
    """
    return settings.host


@pytest.fixture
def http_get_request(base_url: str) -> Callable[..., requests.Response]:
    """
    Fixture for making HTTP GET requests to the API.

    Args:
        base_url: The base URL of the API endpoint.

    Returns:
        Function that makes a HTTP GET request to the API.
    """

    def _make_request(endpoint: str = "/", params: Optional[dict] = None) -> requests.Response:
        """
        Make an HTTP GET request to the API.

        Args:
            endpoint: The endpoint of the API. Defaults to "/".
            params: Optional parameters to be passed in the request

        Returns:
            The response object.
        """
        url = f"{base_url}{endpoint}"
        response = requests.get(url, params=params, timeout=30)
        return response

    return _make_request


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Adds a command-line option to pytest for specifying the environment.

    Args:
        parser: The pytest argument parser.

    Options:
        --env: The environment option to specify the environment mode. Choices are "development" or "production".
               Default is "production".

    Returns:
        None
    """
    parser.addoption(
        "--env",
        action="store",
        default="production",
        choices=["development", "production"],
        help="Environment: development or production",
    )


def pytest_configure(config: pytest.Config) -> None:
    """
    Configures pytest with the specified environment.

    Args:
        config: The pytest config object.

    Returns:
        None
    """
    env = config.getoption("--env")
    settings.setenv(env)
