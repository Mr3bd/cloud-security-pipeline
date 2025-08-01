provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "example-insecure-bucket"
  acl    = "public-read"  # ❌ This is insecure and will be flagged

  versioning {
    enabled = false  # ❌ Versioning disabled (bad practice)
  }

  tags = {
    Environment = "Dev"
    Owner       = "You"
  }
}
