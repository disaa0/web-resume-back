resource "aws_s3_bucket_versioning" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id
  versioning_configuration {
    status = "Disabled"
  }
}