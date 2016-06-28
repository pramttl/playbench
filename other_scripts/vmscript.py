from subprocess import call

url = 'qemu:///system '
management_string = 'virsh -c '
base_command = management_string + url

def listvms():
    command = base_command + ' list --all'
    call(command,shell=True)

def create_vm(config_file):
    command = base_command + 'define ' + config_file
    call(command,shell=True)

def destroy_vm(vm_name):
    command = base_command + "undefine " + vm_name
    call(command,shell=True)

def create_network(config_file):
    command = base_command + "net-define " + config_file
    call(command,shell=True)

def delete_network(network_name):
    command = base_command + "net-undefine " + network_name
    call(command,shell=True)

def start_vm(vmname):
    command = base_command + "start " + vmname
    call(command,shell=True)

def shutdown_vm(vmname):
    command = base_command + "shutdown " + vmname
    call(command,shell=True)

def generate_vm_config(template,vm_name,img_path):
    #replace the vm_name and path
    print 1

def start_network(network_name):
    command = base_command + "net-start " + vmname
    call(command,shell=True)

def stop_network(network):
    command = base_command + "net-destroy " + vmname
    call(command,shell=True)


#listvms()
#create_vm('ubuntu_vm1.xml')
#create_vm('ubuntu.xml')
start_vm('ubuntu_vm1.xml')
listvms()
#destroy_vm('generic')