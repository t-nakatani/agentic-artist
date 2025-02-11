# ECSタスク実行ロール
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "${var.app_name}-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# ECSタスク実行ロールにポリシーをアタッチ
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# S3アクセス用のIAMポリシー
resource "aws_iam_role_policy" "ecs_task_s3_policy" {
  count  = var.env_files != null ? 1 : 0
  name   = "${var.app_name}-s3-policy"
  role   = aws_iam_role.ecs_task_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject"
        ]
        Resource = [
          for env_file in var.env_files : env_file.value
        ]
      }
    ]
  })
}

# S3アクセス用のポリシーをECSタスク実行ロールにアタッチ
resource "aws_iam_role_policy_attachment" "ecs_task_s3_policy_attachment" {
  count      = var.env_files != null ? 1 : 0
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}
