resource "aws_s3_bucket_server_side_encryption_configuration" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id

  rule {
     apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
      bucket_key_enabled = "true"
  }
}