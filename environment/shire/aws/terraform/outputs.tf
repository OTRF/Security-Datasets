output "Region" {
  value = var.region
}
output "EMPIRE_public_ip" {
  value = aws_instance.empire.public_ip
}
output "Apache_Guacamole_public_ip" {
  value = "https://${aws_instance.guac.public_ip}:8443/guacamole"
}

output "HFDC1_public_ip" {
  value = aws_instance.dc.public_ip
}

output "HELK_public_ip" {
  value = aws_instance.helk.public_ip
}

output "WEC_public_ip" {
  value = aws_instance.wec.public_ip
}

output "ACCT001_public_ip" {
  value = aws_instance.acct001.public_ip
}

output "IT001_public_ip" {
  value = aws_instance.it001.public_ip
}

output "HR001_public_ip" {
  value = aws_instance.hr001.public_ip
}

output "HELK_Kibana"{
 value = "https://${aws_instance.helk.public_ip}"
}
