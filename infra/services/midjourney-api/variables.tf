variable "app_name" {
  description = "アプリケーション名"
  type        = string
  default     = "midjourney-api"
}

variable "container_port" {
  description = "コンテナのポート番号"
  type        = number
  default     = 3000
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

variable "desired_count" {
  description = "実行するタスクの数"
  type        = number
  default     = 1
}

variable "assign_public_ip" {
  description = "パブリックIPを割り当てるかどうか"
  type        = bool
  default     = true
}

variable "vpc_id" {
  description = "使用するVPCのID"
  type        = string
}

variable "subnet_ids" {
  description = "使用するサブネットのID一覧"
  type        = list(string)
} 