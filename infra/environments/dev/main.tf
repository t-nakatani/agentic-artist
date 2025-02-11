locals {
  env_files = [
    {
      value = "arn:aws:s3:::lud-env-files/heterod0x/agentic-artist/.env",
      type  = "s3"
    }
  ]
}
module "post_new_art" {
  source = "../../services/post-new-art"

  app_name       = "post-new-art-dev"
  vpc_cidr       = "10.1.0.0/16"
  container_port = var.container_port
  cpu            = var.cpu
  memory         = var.memory
  env_files = local.env_files

  desired_count    = 1
  assign_public_ip = true
}
