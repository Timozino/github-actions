import pytest
from unittest.mock import patch
from io import BytesIO
from script import get_job_postings, output_jobs_to_xls

@pytest.fixture
def mock_remote_ok_response():
    # This mock response simulates the JSON data returned by the Remote OK API
    return [
        {
            "title": "Software Engineer",
            "company": "Example Company",
            "location": "Remote",
            "url": "https://example.com/job/1",
        },
        # Add more job entries as needed for testing different scenarios
    ]

def test_output_jobs_to_xls(mock_remote_ok_response):
    with patch('script.requests.get') as mock_get:
        # Mock the requests.get function to return the simulated API response
        mock_get.return_value.json.return_value = mock_remote_ok_response

        # Use BytesIO to capture the generated Excel file content
        output_file = BytesIO()

        # Run the script with the mocked API response
        output_jobs_to_xls(mock_remote_ok_response)

        # Validate the generated Excel file content
        # You might need to adjust this based on the actual structure of your data
        expected_content = b'\x0... (replace with the expected binary content of the Excel file)'
        assert output_file.getvalue() == expected_content

# Run the test using the following command in your terminal:
# pytest test_script.py
