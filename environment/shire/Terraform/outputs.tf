output "Region" {
  value = var.region
}

output "HELK_public_ip" {
  value = aws_instance.helk.public_ip
}

output "HRDC_public_ip" {
  value = aws_instance.dc.public_ip
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

output "HELK_spark"{
 value = "https://${aws_instance.helk.public_ip}:8080"
}

output "HELK_Jupyter"{
 value = "https://${aws_instance.helk.public_ip}/jupyter"
}

output "HELK_KSQL_Server"{
 value = "https://${aws_instance.helk.public_ip}:8088"
}

output "Empire" {
  value = aws_instance.empire.public_ip
}

output "Apache_Guacamole"{
 value = "https://${aws_instance.empire.public_ip}:8443/guacamole"
}
