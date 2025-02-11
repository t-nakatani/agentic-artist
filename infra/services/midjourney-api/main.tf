module "ecr" {
  source = "../../modules/ecr"

  app_name = var.app_name
}

module "ecs" {
  source = "../../modules/ecs"

  app_name           = var.app_name
  vpc_id             = var.vpc_id
  subnet_ids         = var.subnet_ids
  container_port     = var.container_port
  cpu                = var.cpu
  memory             = var.memory
  ecr_repository_url = module.ecr.repository_url
  env_files          = var.env_files
  env_variables      = var.env_variables
  assign_public_ip   = false  # プライベートサブネットで実行するため
} 