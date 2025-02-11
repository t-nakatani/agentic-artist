resource "aws_security_group" "ecs_tasks" {
  name        = "${var.app_name}-ecs-tasks"
  description = "Allow inbound traffic for ECS tasks"
  vpc_id      = var.vpc_id

  # post-new-artコンテナ用のインバウンドルール
  ingress {
    from_port       = var.container_port
    to_port         = var.container_port
    protocol        = "tcp"
  }

  # midjourney-apiコンテナ用のインバウンドルール
  ingress {
    from_port       = 3000
    to_port         = 3000
    protocol        = "tcp"
  }

  # コンテナ間通信用のインバウンドルール
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    self      = true
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.app_name}-ecs-tasks"
  }
}
