output "gke_name" {
  value = google_container_cluster.gke.name
}

output "gke_zone" {
  value = var.zone
}