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

variable "post_new_art_env_files" {
  description = "コンテナの環境変数"
  type = list(map(string))
  default = null
}

variable "midjourney_env_files" {
  type        = list(map(string))
  description = "Midjourney APIの環境変数ファイル"
  default     = null
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
