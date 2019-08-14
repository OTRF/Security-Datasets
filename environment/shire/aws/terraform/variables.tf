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


#RTO AMI
data "aws_ami" "rto_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["ubuntu18"]
  }
}

#Guacamole 
data "aws_ami" "guac_ami" {
  owners = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20190628"]
  }
}

#HELK Pre-built AMI
data "aws_ami" "helk_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["ubuntu18"]
  }
}
#HFDC1 Pre-built AMI
data "aws_ami" "dc_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["dcserver2016"]
  }
}

#WEC Pre-built AMI
data "aws_ami" "wec_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["wecserver2016"]
  }
}

#ACCT001 Pre-built AMI
data "aws_ami" "acct001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["acct-001"]
  }
}

#IT001 Pre-built AMI
data "aws_ami" "it001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["it-001"]
  }
}

#HR001 Pre-built AMI
data "aws_ami" "hr001_ami" {
  owners = ["946612485350"]
  filter {
    name   = "name"
    values = ["hr-001"]
  }
}




# If you are building your own AMIs you will have replace these values below with your own AMIs. 
# This will also have to be changed if you choose to be in another region besides 'us-west-1'


variable "guac_ami" {
  type    = string
  default = "ami-09eb5e8a83c7aa890"
}

variable "rto_ami" {
  type    = string
  default = "ami-0768b208e80fa3bce"
}

variable "helk_ami" {
  type    = string
  default = "ami-0768b208e80fa3bce"
}

variable "dc_ami" {
  type    = string
  default = "ami-06ae5865adb6ea03e"
}
variable "wec_ami" {
  type    = string
  default = "ami-072ed041a0019650f"
}
variable "acct001_ami" {
  type    = string
  default = "ami-080f7f71f18d03dd2"
}
variable "hr001_ami" {
  type    = string
  default = "ami-0ac047bac6965af66"
}
variable "it001_ami" {
  type    = string
  default = "ami-067631fc05f46ab22"
}
