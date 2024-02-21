import pytest

from ...services.localization_service import format_number_as_pound_value_commas


@pytest.mark.parametrize("test_input, test_output", [
    (1000, "£1,000"),
    (2000000, "£2,000,000"),
    (123456789, "£123,456,789")
])
def test_format_number_with_commas(test_input, test_output):
    assert format_number_as_pound_value_commas(test_input) == test_output
