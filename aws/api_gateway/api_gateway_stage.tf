resource "aws_api_gateway_stage" "test-stage" {
  cache_cluster_enabled = "false"
  deployment_id         = aws_api_gateway_deployment.deployment.id
  rest_api_id           = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  stage_name            = "test"
  xray_tracing_enabled  = "false"
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id

  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.body))
  }

  lifecycle {
    create_before_destroy = true
  }
}