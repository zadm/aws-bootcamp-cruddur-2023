resource "aws_cognito_user_pool" "cruddur_user_pool" {
  name = "cruddur-user-pool-tf"

  # alias_attributes = [
  #   "email",
  # ]

  username_attributes = ["email", "user_name"]
  auto_verified_attributes = ["email"]
  password_policy {
    minimum_length = 6
  }
  username_configuration {
    case_sensitive = true
  }


  verification_message_template {
    default_email_option = "CONFIRM_WITH_CODE"
    email_subject = "Crddur Account Confirmation"
    email_message = "Your confirmation code is {####}"
  }
  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "email"
    required                 = true

    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }

  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "name"
    required                 = true

    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }
  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "preferred_username"
    required                 = true

    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }
}
resource "aws_cognito_user_pool_client" "client" {
  name = "cruddur"

  user_pool_id = aws_cognito_user_pool.cruddur_user_pool.id
  generate_secret = false
  refresh_token_validity = 90
  prevent_user_existence_errors = "ENABLED"
  # explicit_auth_flows = [
  #   "ALLOW_REFRESH_TOKEN_AUTH",
  #   "ALLOW_USER_PASSWORD_AUTH",
  #   "ALLOW_ADMIN_USER_PASSWORD_AUTH"
  # ]
  
}

# resource "aws_cognito_user_pool_domain" "cognito-domain" {
#   domain       = "zk15"
#   user_pool_id = "${aws_cognito_user_pool.cruddur_user_pool.id}"
# }