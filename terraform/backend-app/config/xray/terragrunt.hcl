terraform {
  source = "${get_parent_terragrunt_dir()}/../stacks//xray" # double slash (//) is required

}
include {
  path = find_in_parent_folders()
}