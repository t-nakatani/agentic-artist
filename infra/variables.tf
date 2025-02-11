variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs"
  type        = list(string)
}

variable "app_name" {
  description = "アプリケーション名"
  type        = string
  default     = "post-new-art"
}

variable "container_port" {
  description = "コンテナのポート番号"
  type        = number
  default     = 8000
}

variable "cpu" {
  description = "タスク定義のCPUユニット"
  type        = number
  default     = 256
}

variable "memory" {
  description = "タスク定義のメモリ(MB)"
  type        = number
  default     = 512
}

variable "vpc_cidr" {
  description = "VPCのCIDRブロック"
  type        = string
  default     = "10.0.0.0/16"
}

variable "az_count" {
  description = "使用するアベイラビリティゾーンの数"
  type        = number
  default     = 2
}
