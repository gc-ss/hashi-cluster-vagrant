import json
from pprint import pprint


EXAMPLE = """
[
   {
      "Node":{
         "ID":"e9d282bd-8a49-b7c3-8157-54ba99f523ee",
         "Node":"hashi-client-1",
         "Address":"172.20.20.15",
         "Datacenter":"dc1",
         "TaggedAddresses":{
            "lan":"172.20.20.15",
            "lan_ipv4":"172.20.20.15",
            "wan":"172.20.20.15",
            "wan_ipv4":"172.20.20.15"
         },
         "Meta":{
            "consul-network-segment":""
         },
         "CreateIndex":63,
         "ModifyIndex":68
      },
      "Service":{
         "Kind":"connect-proxy",
         "ID":"_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http-sidecar-proxy",
         "Service":"count-webserver-sidecar-proxy",
         "Tags":[
            
         ],
         "Address":"172.20.20.15",
         "TaggedAddresses":{
            "lan_ipv4":{
               "Address":"172.20.20.15",
               "Port":25313
            },
            "wan_ipv4":{
               "Address":"172.20.20.15",
               "Port":25313
            }
         },
         "Meta":{
            "external-source":"nomad"
         },
         "Port":25313,
         "Weights":{
            "Passing":1,
            "Warning":1
         },
         "EnableTagOverride":false,
         "Proxy":{
            "DestinationServiceName":"count-webserver",
            "DestinationServiceID":"_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http",
            "LocalServiceAddress":"127.0.0.1",
            "LocalServicePort":27962,
            "Config":{
               "bind_address":"0.0.0.0",
               "bind_port":25313,
               "protocol":"http"
            },
            "Upstreams":[
               {
                  "DestinationType":"service",
                  "DestinationName":"redis-db",
                  "Datacenter":"",
                  "LocalBindPort":16379,
                  "MeshGateway":{
                     
                  }
               }
            ],
            "MeshGateway":{
               
            },
            "Expose":{
               
            }
         },
         "Connect":{
            
         },
         "CreateIndex":413,
         "ModifyIndex":413
      },
      "Checks":[
         {
            "Node":"hashi-client-1",
            "CheckID":"serfHealth",
            "Name":"Serf Health Status",
            "Status":"passing",
            "Notes":"",
            "Output":"Agent alive and reachable",
            "ServiceID":"",
            "ServiceName":"",
            "ServiceTags":[
               
            ],
            "Type":"",
            "Definition":{
               
            },
            "CreateIndex":63,
            "ModifyIndex":63
         },
         {
            "Node":"hashi-client-1",
            "CheckID":"service:_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http-sidecar-proxy:1",
            "Name":"Connect Sidecar Listening",
            "Status":"passing",
            "Notes":"",
            "Output":"TCP connect 127.0.0.1:25313: Success",
            "ServiceID":"_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http-sidecar-proxy",
            "ServiceName":"count-webserver-sidecar-proxy",
            "ServiceTags":[
               
            ],
            "Type":"tcp",
            "Definition":{
               
            },
            "CreateIndex":413,
            "ModifyIndex":428
         },
         {
            "Node":"hashi-client-1",
            "CheckID":"service:_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http-sidecar-proxy:2",
            "Name":"Connect Sidecar Aliasing _nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http",
            "Status":"passing",
            "Notes":"",
            "Output":"All checks passing.",
            "ServiceID":"_nomad-task-0b0046db-0bd5-9da6-2ba5-26e35dbee396-group-count-service-group-count-webserver-http-sidecar-proxy",
            "ServiceName":"count-webserver-sidecar-proxy",
            "ServiceTags":[
               
            ],
            "Type":"alias",
            "Definition":{
               
            },
            "CreateIndex":413,
            "ModifyIndex":430
         }
      ]
   }
]
"""

JSON_ST = """
[{"Node":{"ID":"a8fdde55-626b-3cdb-c81f-2c85efd4d3d4", "Node":"hashi-client-1", "Address":"172.20.20.15", "Datacenter":"dc1", "TaggedAddresses":{"lan":"172.20.20.15", "lan_ipv4":"172.20.20.15", "wan":"172.20.20.15", "wan_ipv4":"172.20.20.15"}, "Meta":{"consul-network-segment":""}, "CreateIndex":63, "ModifyIndex":68}, "Service":{"Kind":"connect-proxy", "ID":"_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http-sidecar-proxy", "Service":"count-webserver-sidecar-proxy", "Tags":[], "Address":"172.20.20.15", "TaggedAddresses":{"lan_ipv4":{"Address":"172.20.20.15", "Port":25087}, "wan_ipv4":{"Address":"172.20.20.15", "Port":25087}}, "Meta":{"external-source":"nomad"}, "Port":25087, "Weights":{"Passing":1, "Warning":1}, "EnableTagOverride":false, "Proxy":{"DestinationServiceName":"count-webserver", "DestinationServiceID":"_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http", "LocalServiceAddress":"127.0.0.1", "LocalServicePort":28852, "Config":{"bind_address":"0.0.0.0", "bind_port":25087}, "MeshGateway":{}, "Expose":{}}, "Connect":{}, "CreateIndex":380, "ModifyIndex":380}, "Checks":[{"Node":"hashi-client-1", "CheckID":"serfHealth", "Name":"Serf Health Status", "Status":"passing", "Notes":"", "Output":"Agent alive and reachable", "ServiceID":"", "ServiceName":"", "ServiceTags":[], "Type":"", "Definition":{}, "CreateIndex":63, "ModifyIndex":63},{"Node":"hashi-client-1", "CheckID":"service:_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http-sidecar-proxy:1", "Name":"Connect Sidecar Listening", "Status":"passing", "Notes":"", "Output":"TCP connect 127.0.0.1:25087: Success", "ServiceID":"_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http-sidecar-proxy", "ServiceName":"count-webserver-sidecar-proxy", "ServiceTags":[], "Type":"tcp", "Definition":{}, "CreateIndex":380, "ModifyIndex":401},{"Node":"hashi-client-1", "CheckID":"service:_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http-sidecar-proxy:2", "Name":"Connect Sidecar Aliasing _nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http", "Status":"passing", "Notes":"", "Output":"All checks passing.", "ServiceID":"_nomad-task-fd3fcfca-d823-611e-2e35-d0f4a577fa5f-group-count-service-group-count-webserver-http-sidecar-proxy", "ServiceName":"count-webserver-sidecar-proxy", "ServiceTags":[], "Type":"alias", "Definition":{}, "CreateIndex":380, "ModifyIndex":400}]}]
"""

JSON_ST = """
[{"Node":{"ID":"cfd73ad7-1c86-c953-aa0e-e108bfe799ea","Node":"hashi-client-2","Address":"172.20.20.16","Datacenter":"dc1","TaggedAddresses":{"lan":"172.20.20.16","lan_ipv4":"172.20.20.16","wan":"172.20.20.16","wan_ipv4":"172.20.20.16"},"Meta":{"consul-network-segment":""},"CreateIndex":62,"ModifyIndex":65},"Service":{"Kind":"connect-proxy","ID":"_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080-sidecar-proxy","Service":"count-webserver-sidecar-proxy","Tags":[],"Address":"172.20.20.16","TaggedAddresses":{"lan_ipv4":{"Address":"172.20.20.16","Port":22449},"wan_ipv4":{"Address":"172.20.20.16","Port":22449}},"Meta":{"external-source":"nomad"},"Port":22449,"Weights":{"Passing":1,"Warning":1},"EnableTagOverride":false,"Proxy":{"DestinationServiceName":"count-webserver","DestinationServiceID":"_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080","LocalServiceAddress":"127.0.0.1","LocalServicePort":8080,"Config":{"bind_address":"0.0.0.0","bind_port":22449},"MeshGateway":{},"Expose":{}},"Connect":{},"CreateIndex":3996,"ModifyIndex":3996},"Checks":[{"Node":"hashi-client-2","CheckID":"serfHealth","Name":"Serf Health Status","Status":"passing","Notes":"","Output":"Agent alive and reachable","ServiceID":"","ServiceName":"","ServiceTags":[],"Type":"","Definition":{},"CreateIndex":62,"ModifyIndex":62},{"Node":"hashi-client-2","CheckID":"service:_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080-sidecar-proxy:1","Name":"Connect Sidecar Listening","Status":"passing","Notes":"","Output":"TCP connect 127.0.0.1:22449: Success","ServiceID":"_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080-sidecar-proxy","ServiceName":"count-webserver-sidecar-proxy","ServiceTags":[],"Type":"tcp","Definition":{},"CreateIndex":3996,"ModifyIndex":4006},{"Node":"hashi-client-2","CheckID":"service:_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080-sidecar-proxy:2","Name":"Connect Sidecar Aliasing _nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080","Status":"passing","Notes":"","Output":"No checks found.","ServiceID":"_nomad-task-86e123af-332f-340b-641f-2f66e81f7658-group-count-service-group-count-webserver-8080-sidecar-proxy","ServiceName":"count-webserver-sidecar-proxy","ServiceTags":[],"Type":"alias","Definition":{},"CreateIndex":3996,"ModifyIndex":3996}]}]
"""

# curl "http://127.0.0.1:8500/v1/health/connect/count-webserver?connect=true&passing=1&stale=&token=84f26


def main():
    resp_data = json.loads(JSON_ST)

    for di in resp_data:
        result_di = {
            'Service.Proxy.LocalServiceAddress': di['Service']['Proxy']['LocalServiceAddress'],
            'Service.Proxy.LocalServicePort': di['Service']['Proxy']['LocalServicePort'],
            'Service.Proxy.Config.bind_address': di['Service']['Proxy']['Config']['bind_address'],
            'Service.Proxy.Config.bind_port': di['Service']['Proxy']['Config']['bind_port'],
            'Node.Address': di['Node']['Address'],
            'Node.TaggedAddresses': ','.join(set(di['Node']['TaggedAddresses'].values())),
            'Service.Address': di['Service']['Address'],
            'Service.Port': di['Service']['Port']
        }
        service_tagged_addrs = set()
        for key, addr_di in di['Service']['TaggedAddresses'].items():
            addr = f"{addr_di['Address']}:{addr_di['Port']}"
            service_tagged_addrs.add(addr)
        result_di['Service.TaggedAddresses'] = [s for s in service_tagged_addrs]
        pprint(result_di)

        print('--------------------------')
        listener_public_addr = f"{result_di['Service.Proxy.Config.bind_address']}:{result_di['Service.Proxy.Config.bind_port']}"
        print(f"public address of proxy mTLS listener: {listener_public_addr}")
        local_service_addr = f"{result_di['Service.Proxy.LocalServiceAddress']}:{result_di['Service.Proxy.LocalServicePort']}"
        print(f"local app address that proxy connects to: {local_service_addr}")


if __name__ == '__main__':
    main()
