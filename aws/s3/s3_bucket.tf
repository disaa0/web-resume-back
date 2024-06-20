resource "aws_s3_bucket" "disaadev" {
  bucket        = "disaadev"
  object_lock_enabled = "false"


  tags = {
    crc = "frontend"
  }

  tags_all = {
    crc = "frontend"
  }
}

