resource "aws_api_gateway_integration_response" "met-4su6xysix1-002F-21dp4a-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.res-21dp4a.id

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
    "method.response.header.Access-Control-Allow-Methods" = "'OPTIONS,POST'"
    "method.response.header.Access-Control-Allow-Origin"  = "'https://disaa.dev'"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "met-4su6xysix1-002F-21dp4a-002F-POST-002F-200" {
  http_method = "POST"
  resource_id = aws_api_gateway_resource.res-21dp4a.id

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "'https://disaa.dev'"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "met-4su6xysix1-002F-aocwif-002F-GET-002F-200" {
  http_method = "GET"
  resource_id = aws_api_gateway_resource.res-aocwif.id

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "'https://disaa.dev'"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "met-4su6xysix1-002F-aocwif-002F-OPTIONS-002F-200" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.res-aocwif.id

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS'"
    "method.response.header.Access-Control-Allow-Origin"  = "'https://disaa.dev'"
  }

  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
  status_code = "200"
}
