resource "aws_api_gateway_integration" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS" {
  cache_namespace      = "21dp4a"
  connection_type      = "INTERNET"
  http_method          = "OPTIONS"
  passthrough_behavior = "WHEN_NO_MATCH"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }

  resource_id          = "21dp4a"
  rest_api_id          = "4su6xysix1"
  timeout_milliseconds = "29000"
  type                 = "MOCK"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-21dp4a-002F-POST" {
  cache_namespace         = "21dp4a"
  connection_type         = "INTERNET"
  content_handling        = "CONVERT_TO_TEXT"
  http_method             = "POST"
  integration_http_method = "POST"
  passthrough_behavior    = "WHEN_NO_MATCH"
  resource_id             = "21dp4a"
  rest_api_id             = "4su6xysix1"
  timeout_milliseconds    = "29000"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:767398113748:function:updateVisitors/invocations"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-aocwif-002F-GET" {
  cache_namespace         = "aocwif"
  connection_type         = "INTERNET"
  content_handling        = "CONVERT_TO_TEXT"
  http_method             = "GET"
  integration_http_method = "POST"
  passthrough_behavior    = "WHEN_NO_MATCH"
  resource_id             = "aocwif"
  rest_api_id             = "4su6xysix1"
  timeout_milliseconds    = "29000"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:767398113748:function:getVisitors/invocations"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-aocwif-002F-OPTIONS" {
  cache_namespace      = "aocwif"
  connection_type      = "INTERNET"
  http_method          = "OPTIONS"
  passthrough_behavior = "WHEN_NO_MATCH"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }

  resource_id          = "aocwif"
  rest_api_id          = "4su6xysix1"
  timeout_milliseconds = "29000"
  type                 = "MOCK"
}
