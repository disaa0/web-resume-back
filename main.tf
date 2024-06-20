terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.54.1"
    }
  }
}


module "s3" {
  source = "./aws/s3"
}
module "lambda" {
  source = "./aws/lambda"
}
module "dynamodb" {
  source = "./aws/dynamodb"
}
module "cloudfront" {
  source = "./aws/cloudfront"
}
module "api_gateway" {
  source = "./aws/api_gateway"
}

