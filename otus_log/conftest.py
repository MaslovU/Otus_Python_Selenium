import pytest


def pytest_addoption(parser):
    """Add option"""
    parser.addoption(
        "--path_file",
        action="store",
        help="Path to file"
    )


@pytest.fixture(scope="module")
def get_file_path(driver, request):
    """Get file path"""
    path_file = request.config.getoption("--path_file")
    return path_file
