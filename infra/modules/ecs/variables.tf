variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs"
  type        = list(string)
}

variable "ecr_repository_url" {
  description = "ECR repository URL"
  type        = string
}

variable "app_name" {
  description = "アプリケーション名"
  type        = string
}

variable "container_port" {
  description = "コンテナのポート番号"
  type        = number
}

variable "cpu" {
  description = "タスク定義のCPUユニット"
  type        = number
}

variable "memory" {
  description = "タスク定義のメモリ(MB)"
  type        = number
}

variable "desired_count" {
  description = "実行するタスクの数"
  type        = number
  default     = 1
}

variable "env_files" {
  description = "A list of files to be passed to ECS as environment variables."
  type        = list(object({
    value = string
    type  = string
  }))
  default     = null
}

variable "env_variables" {
  description = "コンテナの環境変数"
  type = list(object({
    name  = string
    value = string
  }))
  default = null
}

variable "assign_public_ip" {
  description = "パブリックIPを割り当てるかどうか"
  type        = bool
  default     = true
} 

variable "log_retention_in_days" {
  description = "CloudWatch Logsの保持期間（日数）"
  type        = number
  default     = 1
}

variable "enable_logging" {
  description = "CloudWatch Logsへのログ出力を有効にするかどうか"
  type        = bool
  default     = true
}

variable "log_configuration" {
  description = "コンテナのログ設定"
  type = object({
    log_driver = string
    options = map(string)
  })
  default = {
    log_driver = "awslogs"
    options = {
      awslogs-stream-prefix = "ecs"
    }
  }
}
