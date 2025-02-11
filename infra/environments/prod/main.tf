module "post_new_art" {
  source = "../../services/post-new-art"

  app_name       = "post-new-art-prod"
  vpc_cidr       = "10.2.0.0/16"
  container_port = var.container_port
  cpu            = var.cpu
  memory         = var.memory
  
  environment_variables = [
    {
      name  = "ENVIRONMENT"
      value = "prod"
    },
    {
      name  = "PYTHONUNBUFFERED"
      value = "1"
    }
  ]
  
  desired_count    = 2
  assign_public_ip = false
} 