resource "aws_ecs_task_definition" "main" {
  family                   = var.app_name
  network_mode            = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                     = var.cpu
  memory                  = var.memory
  execution_role_arn      = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn           = aws_iam_role.ecs_task_role.arn

  container_definitions = jsonencode([
    {
      name      = "post-new-art"
      image     = "${aws_ecr_repository.app.repository_url}:latest"
      essential = true
      portMappings = [
        {
          containerPort = var.container_port
          protocol      = "tcp"
        }
      ]
      environmentFiles = var.post_new_art_env_files

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/${var.app_name}"
          "awslogs-region"        = "ap-northeast-1"
          "awslogs-stream-prefix" = "post-new-art"
        }
      }
      # コンテナ間の依存関係を設定
      dependsOn = [
        {
          containerName = "midjourney-api"
          condition     = "START"
        }
      ]
    },
    {
      name      = "midjourney-api"
      image     = "${aws_ecr_repository.midjourney.repository_url}:latest"
      essential = true
      portMappings = [
        {
          containerPort = 3000
          protocol      = "tcp"
        }
      ]
      environmentFiles = var.midjourney_env_files
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/${var.app_name}"
          "awslogs-region"        = "ap-northeast-1"
          "awslogs-stream-prefix" = "midjourney-api"
        }
      }
    }
  ])

  tags = {
    Name = "${var.app_name}-task-definition"
  }
} 