resource "aws_security_group" "ecs_tasks" {
  name        = "${var.app_name}-ecs-tasks"
  description = "Allow inbound traffic for ECS tasks"
  vpc_id      = var.vpc_id

  # post-new-artコンテナ用のインバウンドルール（APIエンドポイント用）
  ingress {
    from_port       = var.container_port
    to_port         = var.container_port
    protocol        = "tcp"
    cidr_blocks     = ["0.0.0.0/0"]  # APIは外部公開
  }

  # コンテナ間通信用のインバウンドルール（post-new-art -> midjourney-api）
  ingress {
    from_port = 3000
    to_port   = 3000
    protocol  = "tcp"
    self      = true  # 同じセキュリティグループ内からのアクセスのみ許可
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
