# Common Lambda Function Utilities

This directory contains shared utilities for Lambda functions in the resume web application.

## Modules

### dynamodb_utils.py
Provides utilities for:
- DynamoDB connection and error handling
- Standardized API responses with CORS support
- Decimal type handling for JSON serialization
- Event logging

### validation.py
Contains validation functions for:
- Validating visitor count values
- Parsing and validating API Gateway event bodies

## Usage

Import these utilities in your Lambda functions:

```python
import sys
import os

# Add the parent directory to the path to import common modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.dynamodb_utils import get_dynamodb_table, format_response, log_event
from common.validation import validate_visitor_count, parse_event_body
```

## Security Features

- Input validation to prevent invalid data entry
- Proper error handling and logging
- CORS protection
- Rate limiting detection
- Atomic updates with optimistic locking
