resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = "21dp4a"

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "false"
    "method.response.header.Access-Control-Allow-Methods" = "false"
    "method.response.header.Access-Control-Allow-Origin"  = "false"
  }

  rest_api_id = "4su6xysix1"
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-21dp4a-002F-POST-002F-200" {
  http_method = "POST"
  resource_id = "21dp4a"

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "false"
  }

  rest_api_id = "4su6xysix1"
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-aocwif-002F-GET-002F-200" {
  http_method = "GET"
  resource_id = "aocwif"

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "false"
  }

  rest_api_id = "4su6xysix1"
  status_code = "200"
}

resource "aws_api_gateway_method_response" "met-4su6xysix1-002F-aocwif-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = "aocwif"

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "false"
    "method.response.header.Access-Control-Allow-Methods" = "false"
    "method.response.header.Access-Control-Allow-Origin"  = "false"
  }

  rest_api_id = "4su6xysix1"
  status_code = "200"
}
