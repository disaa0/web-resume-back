resource "aws_api_gateway_method" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "OPTIONS"
  resource_id      = aws_api_gateway_resource.res-21dp4a.id
  rest_api_id      = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-21dp4a-002F-POST" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "POST"
  operation_name   = "updateVisitors"
  resource_id      = aws_api_gateway_resource.res-21dp4a.id
  rest_api_id      = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-aocwif-002F-GET" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "GET"
  resource_id      = aws_api_gateway_resource.res-aocwif.id
  rest_api_id      = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-aocwif-002F-OPTIONS" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "OPTIONS"
  resource_id      = aws_api_gateway_resource.res-aocwif.id
  rest_api_id      = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}
