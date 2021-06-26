# taken from https://dev.to/taybenlor/running-vagrant-on-an-m1-apple-silicon-using-docker-3fh4
Vagrant.configure(2) do |config|
  
    # Custom configuration for docker
    config.vm.provider "docker" do |docker, override|
      # docker doesnt use boxes
      override.vm.box = nil
  
      # this is where your Dockerfile lives
      docker.build_dir = "."
  
      # Make sure it sets up ssh with the Dockerfile
      # Vagrant is pretty dependent on ssh
      override.ssh.insert_key = true
      docker.has_ssh = true
  
      # Configure Docker to allow access to more resources
      docker.privileged = true
    end
  
  end