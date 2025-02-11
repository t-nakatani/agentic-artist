# 共有VPCの定義
module "vpc" {
  source = "../../modules/vpc"

  app_name = "shared-vpc-dev"
  vpc_cidr = "10.1.0.0/16"
}

module "post_new_art" {
  source = "../../services/post-new-art"

  app_name       = "post-new-art-dev"
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.subnet_ids
  container_port = 8000
  cpu            = 256
  memory         = 512
  env_files      = local.env_files

  desired_count    = 1
  assign_public_ip = true
}

module "midjourney_api" {
  source = "../../services/midjourney-api"

  app_name       = "midjourney-api-dev"
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.subnet_ids
  container_port = local.midjourney_api_port
  cpu            = 256
  memory         = 512
  env_files      = local.env_files

  desired_count    = 1
  assign_public_ip = false
}
