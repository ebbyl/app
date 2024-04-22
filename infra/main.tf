# ---------------------------------------------------------------------
# Certificate
# ---------------------------------------------------------------------

# Lookup certificate for the domain used to host the application.  

data "aws_acm_certificate" "this" {
  domain   = "*.y4ni.com"
  statuses = ["ISSUED"]
}


# ---------------------------------------------------------------------
# Image
# ---------------------------------------------------------------------

# Lookup the latest image version.

data "aws_ecr_image" "latest" {
  repository_name = "myapp"
  most_recent     = true
}

# ---------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------

locals {
  image = var.image == null ? var.image : data.aws_ecr_image.latest.image_uri
}

module "app" {
  source = "git@github.com:ebbyl/tofu-app-ecs.git?ref=main"

  name     = "ebb"
  image    = local.image
  port     = 8000
  cpu      = 256
  memory   = 512
  replicas = 1

  domain          = "ebb.y4ni.com"
  certificate_arn = data.aws_acm_certificate.this.arn

  tags = local.tags
}

