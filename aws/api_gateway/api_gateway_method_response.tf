resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.res-21dp4a.id

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "false"
    "method.response.header.Access-Control-Allow-Methods" = "false"
    "method.response.header.Access-Control-Allow-Origin"  = "false"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-21dp4a-002F-POST-002F-200" {
  http_method = "POST"
  resource_id = aws_api_gateway_resource.res-21dp4a.id

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "false"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-aocwif-002F-GET-002F-200" {
  http_method = "GET"
  resource_id = aws_api_gateway_resource.res-aocwif.id

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "false"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-aocwif-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.res-aocwif.id

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "false"
    "method.response.header.Access-Control-Allow-Methods" = "false"
    "method.response.header.Access-Control-Allow-Origin"  = "false"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}
