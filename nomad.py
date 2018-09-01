'''
    Datacenter model: ... ;

    Goals:
    - treat the entire datacenter as a collection of resources
    - be able to support non-containerized work loads [do everything at scale across platforms]
    - support continuity (by commanding and controlling a whole lot of stuff at once)
    - schedule things quickly and easily for deployment

    * Can schedule VM's, containers, static binaries, etc.
    - "optimistically concurrent": schedules fast at a large scale ;

    * Try to do things in parallel to reduce wait time ;

'''

# "C-2 level, military grade, crypto security"

terms = {

    "node": ["A physical or virtual machine in a cluster", "A machine running the nomad agent"],
    "nomad agent": ["a long running daemon", "every member of the cluster has", "runs in client mode", "server mode",
                    "is able to run in either mode"],
    "client mode": ["will fingerprint the host", "determine cabilities, resources, and available drivers",
                    "has drivers at its disposal"],
    "server mode": ["has the global state of the cluster", "participates in the scheduling decisions"],
    "job": ["definition of how a workload should be scheduled", "composed of 1 or more task groups"],
    "task group": ["a collection of individual tasks", "co-located on one node", "same node",
                   "for apps that require low latency or high throughput", "in kubernetes, called a pod"],
    "task(s)": ["defines a series of resource constraints and configurations", "a set of work to be executed", "get(s) executed but [their] driver"],
    "job file": ["describes how a workload should be scheduled ;", "A configuration file located on disk ;",
                 "Can be HCL or JSON ;"],
    "driver": ["pluggable component", "executes a task", "provides resource isolation", "docker", "java", "raw-exec",
               "raw exec"],
    "evaluation": ["calculation performed by nomad servers", "determine what actions need to take place to execute a job"],
    "datacenter": ["a private networking env", "low latency", "high bandwidth"],
    "concensus": ["an agreement between leaders / managers"],
    "managers": ["equally ranked"],
    "gossip": ["node-to-node communication", "primarily over UDP", "provides membership", "failure detection",
               "broadcasts info to whole cluster", "built in Serf", "standard scale used for cluster coordination"],
    "bin-packing": ["an algorithm", "optimizes resource utilization", "optimizes application density",
                    "augmented by affinity and anti-affinity rules", "the opposite of spreading things out",
                    "unlike dealing cards", "puts all eggs in one basket until it's full before moving to the next",
                    "packing a bin", "pros and cons", "keeps other nodes open / free for bigger jobs"]
}


# A specific task runs on a specific machine, which determines the resource constraints "of it"

# Tasks to execute: images firing off a binary, node(s) launching a web application, etc;

