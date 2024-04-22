# ---------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------

# Define tags used to identify the infrastructure resources for 
# this application. 

locals {
  tags = {
    owner     = "product"
    project   = "app"
    component = "product.app"
  }
}
