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

    Nomad is a single stack binary, that can run as client as well as server mode;

    agent(client mode):
    The agent is reponsible for profiling the system,
    and provide "liveness" checks, detects heartbeats;
    They run any task that's given;
    Maintains communication with central servers in order to receive jobs;

    agent(server mode):
    responsible for maintaining the data set of all the resources on on each host;
    scheduling those resources;
    participates in leader elections;
    runs replications when necessary;
    discovers other nomad servers;
    etc. ...

    Start the agent by pointing it to the config file;
    It may be configured to spin up, but not configured to talk to other servers;
    > how to inform the servers and clients of each other in order for them to join ?
    This can be done manually or automated;
    Chicken and egg problem with manual bootstrapping: doesn't require any initial tooling,
        but does require some operator participation ;
        > when a client is getting initially started, it has to be informed of at least one nomad server ;
        So one server has to be fully bootstrapped and running until the rest ... ;
        Adds additional provisioning time, delays ;
        Order dependency issues ;

        0 - bootstrap a single nomad server
        1 - catch it's IP address
        2 - put it in configuration


    config flag can be used multiple times in one nomad agent command;

    [bootstrap_expect = 3]: if we had a high availability clust of... say 5, 3 would be the majority ;

    Each server joins just one other server, and learns about the rest via gossip protocol -
    > have them all learn about 1 IP address and they can all learn about each other ;

    On the client side:
    > Address of servers are expected to be available with the client config file;

    If set up in automatic mode: leverage a different tool >> Consul ;

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

# Constraints get enforced by schedulers
service_schedular = "ranks a large portion of the nodes that meet the job criteria, " \
                    "and selects the optimal node in order to place a task group"

schedular_job_types = {
    'service': ["for scheduling long lived services that should never go down", "a daemon process"],
    'batch': ["short lived", "less sensitive to short term performance fluctions",
              "run in the middle of the night when system usage is lower"],
    'system': ["run on all clients which meet the job constraints", "invoked when clients joined cluster",
               "invoked when clients are switched into ready state"]
}


commands = {
    "nomad": "init", # generates a sample job file ;
    "nomad" : "agent -config=/path/to/config.hcl",
    "nomad" : "server-join <known_address>", # currently, there's no equivalent of this for clients: they just connect ;
    "consul" : "",
}



paths = {
    "/etc": "/nomad.d/config.hcl"
}


confighcl = {
    "bootstrap_expect = 3": "at least 3 need to come up before we can reach a quarum and have a majority, and the "
                            "cluster can thus go live ;"

}


questions = {

    "How does a server hold information about other memnbers?" : "", #directory?

}




#  job >
##  group(s) >
###   task(s) >
#########   Resources
#########   Constraints

# There is 1 job definition per file
# job names must be unique within the scope of the entire nomad cluster :
#   "everything gets a name, and every name is unique": this is also common with docker ;











