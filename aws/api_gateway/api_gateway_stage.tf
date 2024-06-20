resource "aws_api_gateway_stage" "test-stage" {
  cache_cluster_enabled = "false"
  deployment_id         = "cooreh"
  rest_api_id           = "4su6xysix1"
  stage_name            = "test"
  xray_tracing_enabled  = "false"
}
