aws_region           = "ap-south-2"
project_name         = "devsecops-gitops-platform"
environment          = "dev"
image_tag_mutability = "MUTABLE"

vpc_cidr             = "10.0.0.0/16"
public_subnet_a_cidr = "10.0.1.0/24"
public_subnet_b_cidr = "10.0.2.0/24"

allowed_ssh_cidrs = ["0.0.0.0/0"]
allowed_app_cidrs = ["0.0.0.0/0"]

app_port      = 8000
instance_type = "t3.micro"
key_pair_name = ""