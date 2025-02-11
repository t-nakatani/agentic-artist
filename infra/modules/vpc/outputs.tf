output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "subnet_ids" {
  description = "サブネットのID一覧"
  value       = aws_subnet.public[*].id
}
