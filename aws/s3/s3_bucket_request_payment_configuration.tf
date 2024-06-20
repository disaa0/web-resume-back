resource "aws_s3_bucket_request_payment_configuration" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id
  payer  = "BucketOwner"
}