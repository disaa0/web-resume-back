data "archive_file" "getVisitors" {
  type        = "zip"
  source_file = "./src/lambda_functions/getVisitors/lambda_function.py"
  output_path = "./src/lambda_functions/getVisitors/lambda_function.zip"
}

resource "aws_lambda_function" "getVisitors" {
  architectures = ["arm64"]

  ephemeral_storage {
    size = "512"
  }

  function_name = "getVisitors"
  handler       = "lambda_function.lambda_handler"
  

  logging_config {
    log_format = "Text"
    log_group  = "/aws/lambda/getVisitors"
  }

  memory_size                    = "128"
  package_type                   = "Zip"
  reserved_concurrent_executions = "-1"
  role                           = "arn:aws:iam::767398113748:role/service-role/getVisitors-role-41obggnz"
  runtime                        = "python3.12"
  skip_destroy                   = "false"
  timeout                        = "3"
  filename                       = "./src/lambda_functions/getVisitors/lambda_function.zip"

  source_code_hash = data.archive_file.getVisitors.output_base64sha256
  
  tracing_config {
    mode = "PassThrough"
  }
}

data "archive_file" "updateVisitors" {
  type        = "zip"
  source_file = "./src/lambda_functions/updateVisitors/lambda_function.py"
  output_path = "./src/lambda_functions/updateVisitors/lambda_function.zip"
}

resource "aws_lambda_function" "updateVisitors" {
  architectures = ["arm64"]

  ephemeral_storage {
    size = "512"
  }

  function_name = "updateVisitors"
  handler       = "lambda_function.lambda_handler"

  logging_config {
    log_format = "Text"
    log_group  = "/aws/lambda/updateVisitors"
  }

  memory_size                    = "128"
  package_type                   = "Zip"
  reserved_concurrent_executions = "-1"
  role                           = "arn:aws:iam::767398113748:role/service-role/updateVisitors-role-c7y301jo"
  runtime                        = "python3.12"
  skip_destroy                   = "false"
  timeout                        = "3"
  filename                       = "./src/lambda_functions/updateVisitors/lambda_function.zip"

  source_code_hash = data.archive_file.updateVisitors.output_base64sha256

  tracing_config {
    mode = "PassThrough"
  }
}
