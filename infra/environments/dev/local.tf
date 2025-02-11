locals {
  midjourney_api_port = 3000
  env_files = [
    {
      value = "arn:aws:s3:::lud-env-files/heterod0x/agentic-artist/.env",
      type  = "s3"
    }
  ]

  env_variables = [
    {
      name  = "ENVIRONMENT"
      value = "dev"
    }
  ]
}
