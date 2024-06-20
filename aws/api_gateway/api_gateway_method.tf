resource "aws_api_gateway_method" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "OPTIONS"
  resource_id      = "21dp4a"
  rest_api_id      = "4su6xysix1"
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-21dp4a-002F-POST" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "POST"
  operation_name   = "updateVisitors"
  resource_id      = "21dp4a"
  rest_api_id      = "4su6xysix1"
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-aocwif-002F-GET" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "GET"
  resource_id      = "aocwif"
  rest_api_id      = "4su6xysix1"
}

resource "aws_api_gateway_method" "met-4su6xysix1-002F-aocwif-002F-OPTIONS" {
  api_key_required = "false"
  authorization    = "NONE"
  http_method      = "OPTIONS"
  resource_id      = "aocwif"
  rest_api_id      = "4su6xysix1"
}
