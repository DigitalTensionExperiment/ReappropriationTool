
ping = "how long it takes a request to go to a server and come back, an amount of time, milliseconds"
bandwidth = "speed of data going between, amount of data, the amount of data moving per sec"


terms = ["component", "scheduling", "cluster", "daemon", "host", "agent", "virtual machine", "cluster coordination",
         "build processes", "build time", "run time", "infrastructure as code", "workload", "resource isolation",
         "Robert's Rules of Order", "short term performance fluctuations"]

general = {
    "workload": "a set of work to be executed",
    "state replication": "consensus"
}

tools_descriptions = {
    "anchor": "Allows creation of custom security policies to be utilized at build time ;",
    "artifactory": "",
    "packer": "Handles automated machine imaging (for AWS machines, etc.);",
    "bitbucket": "",
    "cassandra": "",
    "consul": "each server and client will become aware of each other when a consul agent is installed on each host ; "
              "already multi-dc-aware ; can do health check ; can do service discovery ; cluster-aware Redis, more like Nagios ;",
    "docker": "Allows container creation from image files ;",
    "jenkins": "Runs build processes ;",
    "kafka": "",
    "nginx": "web server ;",
    "nagios": "",
    "nomad": "scheduling and deployments ;",
    "redis": "handles key/value pairs ;",
    "terraform": "Allows infrastructure as code, lifecycle management, service discovery, running healthchecks, distributed key value stores ;",
    "vagrant": "Handles environment provisioning ;",
    "vault": "security",
    "vericode": "",
    "xray": "Artifactory image scanning ;",
}

examples = {
    "service_scheduler": ['webApp', 'redis'],
    "batch_scheduler": ["billing", "data replication"],
    "system_scheduler": ["logging agent", "security auditing tool"]
}


agent_based_technologies = [
    "appDynamics",
    "nomad",
    "consul"
]


DNS = [
    "network distrbuted DB",
    "contains key/value pairs",
    "prior to AD (active directory) or LDAP",
    "CNAME",
    "A records of CNAME",
    "RP (responsible party) records of CNAME",
]

actions = ["executes", "fingerprint", "evaluate the job request", "allocate resources",
           "send info out to the different nodes", "replicate the job", "send [job] into different groups", ]
























