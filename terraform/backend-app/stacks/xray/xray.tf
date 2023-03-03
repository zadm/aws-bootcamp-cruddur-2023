resource "aws_xray_group" "group" {
  group_name        = "${var.environment}-${var.group_name}"
  filter_expression = "service(\"${var.react_app_backend_url}\") {fault OR error}"
  tags = {
    "application_name" : "cruddur",
    "owner" : "zk15.xyz",
    "environment" : "production"
  }
}

resource "aws_xray_sampling_rule" "simple_rule" {
  rule_name      = "Cruddur"
  priority       = 9000
  version        = 1
  reservoir_size = 1
  fixed_rate     = 0.1
  url_path       = "*"
  host           = "*"
  http_method    = "*"
  service_type   = "*"
  service_name   = "Cruddur"
  resource_arn   = "*"
}