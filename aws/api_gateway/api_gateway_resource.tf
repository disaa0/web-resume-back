resource "aws_api_gateway_resource" "res-21dp4a" {
  parent_id   = "ld78n10odb"
  path_part   = "update-visitors"
  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}

resource "aws_api_gateway_resource" "res-aocwif" {
  parent_id   = "ld78n10odb"
  path_part   = "get-visitors"
  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}

resource "aws_api_gateway_resource" "res-ld78n10odb" {
  parent_id   = ""
  path_part   = ""
  rest_api_id = aws_api_gateway_rest_api.api-4su6xysix1_resumeapi.id
}
