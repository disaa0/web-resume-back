resource "aws_s3_bucket_website_configuration" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id

  index_document {
    suffix = "index.html"
  }
}
