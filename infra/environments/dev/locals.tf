locals {
  post_new_art_env_files = [
    {
      value = "arn:aws:s3:::lud-env-files/heterod0x/agentic-artist/artist-agent-api/.env",
      type  = "s3"
    }
  ]

  midjourney_api_env_files = [
    {
      value = "arn:aws:s3:::lud-env-files/heterod0x/agentic-artist/midjourney-api/.env",
      type  = "s3"
    }
  ]
}
