resource "aws_lambda_permission" "getVisitors-AllowExecutionFromAPIGateway" {
  action        = "lambda:InvokeFunction"
  function_name = "arn:aws:lambda:us-east-2:767398113748:function:getVisitors"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:us-east-2:767398113748:4su6xysix1/*/GET/get-visitors"
  statement_id  = "AllowExecutionFromAPIGateway"
}

resource "aws_lambda_permission" "updateVisitors-AllowExecutionFromAPIGateway" {
  action        = "lambda:InvokeFunction"
  function_name = "arn:aws:lambda:us-east-2:767398113748:function:updateVisitors"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:us-east-2:767398113748:4su6xysix1/*/POST/update-visitors"
  statement_id  = "AllowExecutionFromAPIGateway"
}
