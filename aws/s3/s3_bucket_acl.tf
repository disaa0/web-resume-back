resource "aws_s3_bucket_ownership_controls" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_public_access_block" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

data "aws_canonical_user_id" "current" {}

resource "aws_s3_bucket_acl" "disaadev" {
  depends_on = [
    aws_s3_bucket_ownership_controls.disaadev,
    aws_s3_bucket_public_access_block.disaadev,
  ]

  bucket = aws_s3_bucket.disaadev.id
  #acl    = "public-read"
  
  access_control_policy {
    grant {
      grantee {
        id   = data.aws_canonical_user_id.current.id
        type = "CanonicalUser"
      }
      permission = "FULL_CONTROL"
    }
    owner {
      id = data.aws_canonical_user_id.current.id
    }
  }
}