terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "ap-northeast-1"
    encrypt        = true
  }
}

provider "aws" {
  region = "ap-northeast-1"  # リソースのデプロイ先は変更なし

  default_tags {
    tags = {
      Environment = "prod"
      ManagedBy  = "terraform"
    }
  }
} 