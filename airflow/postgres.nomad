# other nomad jobs! https://github.com/GuyBarros/nomad_jobs
# also see: https://github.com/GuyBarros/nomad_jobs/blob/master/boundary-postgres.nomad

job "postgres-task" {
  # based on: https://github.com/ccakes/nomad-pgsql-patroni/blob/master/example-patroni.yml
  type = "service"
  dataceners = ["dc1"]

  vault { policies = ["nomad-client-base"] }

  group "postgres-group" {
    count = 2

    task "postgres-db" {
      driver = "docker"

      template {
        data <<EOL
scope: postgres
name: pg-{{env "node.unique.name"}}
namespace: /nomad

restapi:
  listen: 0.0.0.0:{{env "NOMAD_PORT_api"}}
  connect_address: {{env "NOMAD_ADDR_api"}}

consul:
host: consul.example.com
token: {{with secret "consul/creds/postgres"}}{{.Data.token}}{{end}}
register_service: true

# bootstrap config
EOL
      }

      config {
        image = "ccakes/nomad-pgsql-patroni:13.0-1.gis"

        port_map {
          pg = 5432
          api = 8008
        }
      }

      resources {
        memory = 1024

        network {
          port "api" {}
          port "pg" {}
        }
      }
    }
  }
}
// './example-patroni.yml:/secrets/patroni.yml'