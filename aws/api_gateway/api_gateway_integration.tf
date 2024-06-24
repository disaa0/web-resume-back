resource "aws_api_gateway_integration" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS" {
  cache_namespace      = aws_api_gateway_resource.res-21dp4a.id
  connection_type      = "INTERNET"
  http_method          = "OPTIONS"
  passthrough_behavior = "WHEN_NO_MATCH"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }

  resource_id          = aws_api_gateway_resource.res-21dp4a.id
  rest_api_id          = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  timeout_milliseconds = "29000"
  type                 = "MOCK"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-21dp4a-002F-POST" {
  cache_namespace         = aws_api_gateway_resource.res-21dp4a.id
  connection_type         = "INTERNET"
  content_handling        = "CONVERT_TO_TEXT"
  http_method             = "POST"
  integration_http_method = "POST"
  passthrough_behavior    = "WHEN_NO_MATCH"
  resource_id             = aws_api_gateway_resource.res-21dp4a.id
  rest_api_id             = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  timeout_milliseconds    = "29000"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:767398113748:function:updateVisitors/invocations"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-aocwif-002F-GET" {
  cache_namespace         = aws_api_gateway_resource.res-aocwif.id
  connection_type         = "INTERNET"
  content_handling        = "CONVERT_TO_TEXT"
  http_method             = "GET"
  integration_http_method = "POST"
  passthrough_behavior    = "WHEN_NO_MATCH"
  resource_id             = aws_api_gateway_resource.res-aocwif.id
  rest_api_id             = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  timeout_milliseconds    = "29000"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:767398113748:function:getVisitors/invocations"
}

resource "aws_api_gateway_integration" "met-4su6xysix1-002F-aocwif-002F-OPTIONS" {
  cache_namespace      = aws_api_gateway_resource.res-aocwif.id
  connection_type      = "INTERNET"
  http_method          = "OPTIONS"
  passthrough_behavior = "WHEN_NO_MATCH"

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }

  resource_id          = aws_api_gateway_resource.res-aocwif.id
  rest_api_id          = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  timeout_milliseconds = "29000"
  type                 = "MOCK"
}
