variable "container_port" {
  description = "コンテナのポート番号"
  type        = number
  default     = 8000
}

variable "cpu" {
  description = "タスク定義のCPUユニット"
  type        = number
  default     = 512
}

variable "memory" {
  description = "タスク定義のメモリ(MB)"
  type        = number
  default     = 1024
}

variable "vpc_id" {
  description = "VPC ID for production environment"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs for production environment"
  type        = list(string)
} 