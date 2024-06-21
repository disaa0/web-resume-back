provider "aws" {
  region = "us-east-1"
  profile = "poweruser"
}

terraform {
	required_providers {
		aws = {
	    version = "~> 5.54.1"
		}
  }
}
