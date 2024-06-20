resource "aws_s3_bucket_policy" "disaadev" {
  bucket = aws_s3_bucket.disaadev.id
  policy = data.aws_iam_policy_document.disaadev.json
}

data "aws_iam_policy_document" "disaadev" {
  statement {
    sid = "PublicReadGetObject"
    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]

    resources = [
      aws_s3_bucket.disaadev.arn,
      "${aws_s3_bucket.disaadev.arn}/*",
    ]
  }
}
