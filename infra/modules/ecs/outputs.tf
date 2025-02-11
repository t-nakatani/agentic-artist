output "cluster_name" {
  description = "ECSクラスターの名前"
  value       = aws_ecs_cluster.main.name
}

output "service_name" {
  description = "ECSサービスの名前"
  value       = aws_ecs_service.app.name
}
