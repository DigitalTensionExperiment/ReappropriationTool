//job "" {
  ##----------------------------------------------------------------------------
  # [JOB]
  ##----------------------------------------------------------------------------

  # top level keys :
  # datacenters = [""] # required argument
  # region = "" # default = global
  # type = "" # default = service

  # meta block
  # meta{
    # jenkins_job_file = ""
    # application_meta = ""
    # deployment_file  = ""
  # }

  # will configure the update strategy for the job
  # update{
    # stagger      = "" # updating one at a time, staggering every X seconds
    # max_parallel = 1
    # canary       = 0
  # }





  # Specifies a list of tasks co-located on the same host
//  group "appd_proxy-dev" {
    ##----------------------------------------------------------------------------
    # JOB : [Group]
    ##----------------------------------------------------------------------------

    # ephemeral_disk block: Will need this in order to be able to move this around
    # ephemeral_disk {
      # migrate = # boolean
      # size    = ""
      # sticky  = # boolean
    # }

    # restart block
    # Can a restart block have a task within it?
    # restart {
      # attempts = 5
      # delay    = ""
      # interval = ""
      # mode     = ""
    # }

    # constraint block
    # constraint {
        # attribute = "${}"
        # value     = ""
    # }



//    task "" {
      ##----------------------------------------------------------------------------
      # JOB : Group : [task]
      ##----------------------------------------------------------------------------

      # drivers and driver specific configs
      # The drive executes the task
      # driver = "" (ie: docker)

//      config {

//        logging {
//          type = "" (ie: journald)
            # Why does this config block, inside a config block, have a tag value ?
//          config {
//            tag = ""
//          }
//        }

//        volumes = [
//          "/:/hostroot:ro",
//          "/var/run/docker.sock:/var/run/docker.sock",
//          "/var/run/appd:/var/run/appd"
//        ]
//        image = ""

      ##----------------------------------------------------------------------------
      # JOB : Group : / [task]
      ##----------------------------------------------------------------------------
//      }





      # Does the placement of a service block matter ?
      # service block: specifies how the service should register with the discovery layer (w/ Consul, etc)
      #   service {
      #     ...
      #   }

//      env {
//
//      }

      # resource block: specify the job constrains
//      resources {
//        cpu       = 1000
//        memory    = 1000
//        network {
//          mbits = 1
//        }
//      }

    ##----------------------------------------------------------------------------
    # JOB : / [Group]
    ##----------------------------------------------------------------------------
//    }


  ##----------------------------------------------------------------------------
  # / [JOB]
  ##----------------------------------------------------------------------------
//}
