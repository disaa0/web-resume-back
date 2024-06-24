resource "aws_api_gateway_usage_plan" "default-plan" {
  api_stages {
    api_id = "4su6xysix1"
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
