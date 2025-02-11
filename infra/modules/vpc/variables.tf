variable "app_name" {
  description = "アプリケーション名"
  type        = string
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