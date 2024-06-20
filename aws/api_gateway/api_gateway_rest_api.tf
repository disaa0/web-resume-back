resource "aws_api_gateway_rest_api" "api-4su6xysix1_resumeapi" {
  api_key_source               = "HEADER"
  disable_execute_api_endpoint = "false"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  name = "resumeapi"
}
