# Specify the provider and access details
provider "aws" {
region                  = var.region
}

# Create a VPC to launch our instances into
resource "aws_vpc" "default" {
  cidr_block = "172.18.0.0/16"
}

# Create an internet gateway to give our subnet access to the outside world
resource "aws_internet_gateway" "default" {
  vpc_id = aws_vpc.default.id
}

# Grant the VPC internet access on its main route table
resource "aws_route" "internet_access" {
  route_table_id         = aws_vpc.default.main_route_table_id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.default.id
}

# Create a subnet to launch our instances into
resource "aws_subnet" "default" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = "172.18.39.0/24"
  availability_zone       = var.availability_zone
  map_public_ip_on_launch = true
}

# Adjust VPC DNS settings to not conflict with lab
resource "aws_vpc_dhcp_options" "default" {
  domain_name          = "shire.com"
  domain_name_servers  = concat([aws_instance.dc.private_ip], var.external_dns_servers)
  netbios_name_servers = [aws_instance.dc.private_ip]
 }

resource "aws_vpc_dhcp_options_association" "default" {
  vpc_id          = aws_vpc.default.id
  dhcp_options_id = aws_vpc_dhcp_options.default.id
}

# Security Group for Linux Machines
resource "aws_security_group" "linux" {
  name        = "linux_security_group"
  description = "Mordor: Security Group for the Linux Hosts"
  vpc_id	= aws_vpc.default.id

  # SSH Access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

  # Apache Guacamole Access
  ingress {
    from_port   = 8443
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

  # Zookeeper Access
  ingress {
    from_port   = 2181
    to_port     = 8443
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

    # Apache Spark Access
  ingress {
    from_port   = 8088
    to_port     = 8088
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

    # Kibana Access
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

  # Allow all traffic from the private subnet
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["172.18.39.0/24"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "windows" {
  name        = "mordor_windows_workstations"
  description = "Security Group for Mordor Windows Machines"
  vpc_id      = aws_vpc.default.id

  # RDP
  ingress {
    from_port   = 3389
    to_port     = 3389
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }

  # WinRM
  ingress {
    from_port   = 5985
    to_port     = 5985
    protocol    = "tcp"
    cidr_blocks = var.ip_whitelist
  }


  # Allow all traffic from the private subnet
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["172.18.39.0/24"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "auth" {
  key_name   = var.public_key_name
  public_key = file(var.public_key_path)
}


#HELK Provisioner
resource "aws_instance" "helk" {
  instance_type = "t2.xlarge"
  ami           = coalesce(data.aws_ami.helk_ami.image_id, var.helk_ami)

  tags = {
    Name = "HELK"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.linux.id]
  key_name               = aws_key_pair.auth.key_name
  private_ip             = "172.18.39.6"

  
  # Copying SSH Keys and Update
  provisioner "remote-exec" {
    inline = [
      "sudo cp /home/ubuntu/.ssh/authorized_keys /home/aragon/.ssh/authorized_keys",
      "cd /opt/",
      "sudo git clone https://github.com/Cyb3rWard0g/mordor.git",
      
    ]
      connection {
      host        = coalesce(self.public_ip, self.private_ip)
      type        = "ssh"
      user        = "ubuntu"
      private_key = file(var.private_key_path)
    }
  }
  root_block_device {
    delete_on_termination = true
    volume_size           = 100
  }
}

#Empire 
resource "aws_instance" "empire" {
instance_type = "t2.large"
ami           = coalesce(data.aws_ami.empire_ami.image_id, var.empire_ami)

  tags = {
   Name = "Empire"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.linux.id]
  key_name               = aws_key_pair.auth.key_name
  private_ip             = "172.18.39.8"

  
  # Created User 'wardog'. Copying ssh keys. 
  provisioner "remote-exec" {
    inline = [
     "sudo cp /home/ubuntu/.ssh/authorized_keys /home/wardog/.ssh/authorized_keys",
    ]
     connection {
      host        = coalesce(self.public_ip, self.private_ip)
      type        = "ssh"
      user        = "ubuntu"
      private_key = file(var.private_key_path)
    }
  }
  root_block_device {
   delete_on_termination = true
    volume_size           = 100
  }
}

 # HFDC1.shire.com build
resource "aws_instance" "dc" {
  instance_type = "t2.medium"
  ami = coalesce(data.aws_ami.dc_ami.image_id)

  tags = {
    Name = "HFDC1.shire.com"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.windows.id]
  private_ip             = "172.18.39.5"

  root_block_device {
    delete_on_termination = true
  }
}

 # WECServer Build
resource "aws_instance" "wec" {
  instance_type = "t2.medium"
  ami = coalesce(data.aws_ami.wec_ami.image_id)

  tags = {
    Name = "WECServer.shire.com"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.windows.id]
  private_ip             = "172.18.39.102"

  root_block_device {
    delete_on_termination = true
  }
}

 # ACCT001 Build
resource "aws_instance" "acct001" {
  instance_type = "t2.medium"
  ami = coalesce(data.aws_ami.acct001_ami.image_id)

  tags = {
    Name = "ACCT001.shire.com"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.windows.id]
  private_ip             = "172.18.39.100"

  root_block_device {
    delete_on_termination = true
  }
}

 # HR001 Build
resource "aws_instance" "hr001" {
  instance_type = "t2.medium"
  ami = coalesce(data.aws_ami.hr001_ami.image_id)

  tags = {
    Name = "HR001.shire.com"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.windows.id]
  private_ip             = "172.18.39.106"

  root_block_device {
    delete_on_termination = true
  }
}

 # IT001 Build
resource "aws_instance" "it001" {
  instance_type = "t2.medium"
  ami = coalesce(data.aws_ami.it001_ami.image_id)

  tags = {
    Name = "IT001.shire.com"
  }

  subnet_id              = aws_subnet.default.id
  vpc_security_group_ids = [aws_security_group.windows.id]
  private_ip             = "172.18.39.105"

  root_block_device {
    delete_on_termination = true
  }
}
