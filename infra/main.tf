module "vpc" {
  source = "./modules/vpc"

  app_name = var.app_name
  vpc_cidr = var.vpc_cidr
}

module "ecr" {
  source = "./modules/ecr"

  app_name = var.app_name
}

module "ecs" {
  source = "./modules/ecs"

  app_name           = var.app_name
  vpc_id             = module.vpc.vpc_id
  subnet_ids         = module.vpc.subnet_ids
  container_port     = var.container_port
  cpu                = var.cpu
  memory             = var.memory
  ecr_repository_url = "${module.ecr.repository_url}:latest"
}
