resource "aws_dynamodb_table" "resume" {
  attribute {
    name = "id"
    type = "S"
  }

  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = "false"
  hash_key                    = "id"
  name                        = "resume"

  point_in_time_recovery {
    enabled = "false"
  }

  read_capacity  = "0"
  stream_enabled = "false"
  table_class    = "STANDARD"
  write_capacity = "0"
}
