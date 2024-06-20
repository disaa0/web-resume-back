output "aws_lambda_function_getVisitors_id" {
  value = "${aws_lambda_function.getVisitors.id}"
}

output "aws_lambda_function_updateVisitors_id" {
  value = "${aws_lambda_function.updateVisitors.id}"
}

output "aws_lambda_permission_getVisitors-AllowExecutionFromAPIGateway_id" {
  value = "${aws_lambda_permission.getVisitors-AllowExecutionFromAPIGateway.id}"
}

output "aws_lambda_permission_updateVisitors-AllowExecutionFromAPIGateway_id" {
  value = "${aws_lambda_permission.updateVisitors-AllowExecutionFromAPIGateway.id}"
}
