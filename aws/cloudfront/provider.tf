provider "aws" {
  region = "us-east-1"
  profile = "admin-disaa0"
}

terraform {
	required_providers {
		aws = {
	    version = "~> 5.54.1"
		}
  }
}
