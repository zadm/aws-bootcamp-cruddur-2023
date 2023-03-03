locals {
  default_yaml_path    = find_in_parent_folders("root.yml")
  aws_region           = "eu-west-1"
  environment          = get_env("TF_VAR_ENV", "dev") # "dev" by default to avoid mistakes when developping locally
  project_name         = "cruddur-backend"
  account_name         = "bootcamp"
  app_version          = get_env("PACKAGE_VERSION", "0.0.0")

}

remote_state {
  backend = "s3"
  config = {
    bucket                = "${local.account_name}-${local.environment}-tfstates-bucket"
    key                   = "${local.project_name}/${path_relative_to_include()}/terraform.tfstate"
    region                = local.aws_region
    encrypt               = true
    dynamodb_table        = "${local.account_name}-${local.environment}-tfstatelocks"
    disable_bucket_update = true
  }
}

# Configure root level variables that all resources can inherit
# We do not use .tfvar files because of this issue: https://github.com/gruntwork-io/terragrunt/issues/873
# Solution: we use .vars.yml files. Under the hood, Terragrunt generates TF_VAR_xxx environment variables from them
# Source: https://github.com/gruntwork-io/terragrunt-infrastructure-live-example/blob/master/prod/terragrunt.hcl

# Files are evaluated/overriden into this order (the later takes predecence):
# 0. Inputs defined in this file (main terragrunt.hcl)
# 1. /live/common.vars.yml
# 2. /live/**/common.vars.yml
# 3. /live/<TF_VAR_env>.vars.yml
# 4. /live/**/<TF_VAR_env>.vars.yml
#

inputs = merge(
  {
    project_name : local.project_name,
    aws_region : local.aws_region,
    environment : local.environment,
    app_version : local.app_version,
  },
  try(yamldecode(
    fileexists("${find_in_parent_folders("common.vars.yml", local.default_yaml_path)}") ? file("${find_in_parent_folders("common.vars.yml", local.default_yaml_path)}") : "{}",
  ), {}),
  try(yamldecode(fileexists("${get_terragrunt_dir()}/common.vars.yml") ? file("${get_terragrunt_dir()}/common.vars.yml") : "{}"), {}),
  try(yamldecode(
    fileexists("${find_in_parent_folders("${local.environment}.vars.yml", local.default_yaml_path)}") ? file("${find_in_parent_folders("${local.environment}.vars.yml", local.default_yaml_path)}") : "{}",
  ), {}),
  try(yamldecode(fileexists("${get_terragrunt_dir()}/${local.environment}.vars.yml") ? file("${get_terragrunt_dir()}/${local.environment}.vars.yml") : "{}"), {})
)