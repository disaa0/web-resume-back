resource "aws_api_gateway_usage_plan" "default-plan" {
  api_stages {
    api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
    stage  = "test"
  }

  name = "default plan"

  quota_settings {
    limit  = "50"
    offset = "0"
    period = "DAY"
  }

  throttle_settings {
    burst_limit = "2"
    rate_limit  = "1"
  }
}
