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