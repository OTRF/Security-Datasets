variable "region" {
  default = "us-west-1"
}

variable "profile" {
  default = "terraform"
}

variable "availability_zone" {
  description = "https://www.terraform.io/docs/providers/aws/d/availability_zone.html"
  default     = ""
}

variable "shared_credentials_file" {
  description = "Path to your AWS credentials file"
  type        = string
  default     = "~/.aws/credentials"
}

variable "public_key_name" {
  description = "A name for AWS Keypair to use to auth to helk. Can be anything you specify."
  default     = "linux"
}

variable "public_key_path" {
  description = "Path to the public key to be loaded into the helk authorized_keys file"
  type        = string
  default     = "~/.ssh/linux.pub"
}

variable "private_key_path" {
  description = "Path to the private key to use to authenticate to helk."
  type        = string
  default     = "~/.ssh/linux"
}

variable "ip_whitelist" {
  description = "A list of CIDRs that will be allowed to access the EC2 instances"
  type        = list(string)
  default     = [""]
}

variable "external_dns_servers" {
  description = "Configure lab to allow external DNS resolution"
  type        = list(string)
  default     = ["8.8.8.8"]
}

#Empire AMI
data "aws_ami" "empire_ami" {
  owners = ["946612485350"]
  filter {
   name   = "name"
  values = ["empire"]
  }
}

#HELK Pre-built AMI
data "aws_ami" "helk_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["HELK"]
  }
}

#HFDC Pre-built AMI
data "aws_ami" "dc_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["HFDC1.shire.com"]
  }
}

#ACCT001 Pre-built AMI
data "aws_ami" "acct001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["ACCT001.shire.com"]
  }
}

#IT001 Pre-built AMI
data "aws_ami" "it001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["IT001.shire.com"]
  }
}

#HR001 Pre-built AMI
data "aws_ami" "hr001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["HR001.shire.com"]
  }
}


#WEC Pre-built AMI
data "aws_ami" "wec_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["WECServer.shire.com"]
  }
}

# If you are building your own AMIs you will have replace these values below with your own AMIs. 
# This will also have to be changed if you choose to be in another region besides 'us-west-1'


variable "empire_ami" {
  type    = string
  default = "ami-039e04f44b2a9a69c"
}


variable "helk_ami" {
  type    = string
  default = "ami-02ac0fcda6483ea01"
}

variable "dc_ami" {
  type    = string
  default = "ami-06215d1db6e0b3b3d"
}

variable "wec_ami" {
  type    = string
  default = "ami-07ac570b4e06c6107"
}

variable "acct001_ami" {
  type    = string
  default = "ami-05f416ac453eb9c06"
}

variable "hr001_ami" {
  type    = string
  default = "ami-0fbdf1b6824728392"
}

variable "it001_ami" {
  type    = string
  default = "ami-09015403f377359ce"
}
