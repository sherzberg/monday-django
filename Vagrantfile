Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://dl.dropbox.com/u/1537815/precise64.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000
  
  config.vm.synced_folder ".", "/home/vagrant/monday-django", owner: "vagrant", group: "vagrant"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file = "django.pp"
  end
  
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
  end
end
