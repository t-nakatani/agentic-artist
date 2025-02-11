output "repository_url" {
  description = "ECRリポジトリのURL"
  value       = aws_ecr_repository.app.repository_url
} 