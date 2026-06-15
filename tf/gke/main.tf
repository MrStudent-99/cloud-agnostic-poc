terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.45"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "container" {
  project = var.project_id
  service = "container.googleapis.com"
  disable_on_destroy = false
}

resource "google_container_cluster" "gke" {
  name     = "gke-capoc"
  location = var.zone

  remove_default_node_pool = true
  initial_node_count       = 1

  deletion_protection = false

  depends_on = [google_project_service.container]
}

resource "google_container_node_pool" "nodes" {
  name       = "np-capoc"
  location   = var.zone
  cluster    = google_container_cluster.gke.name
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 100
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}