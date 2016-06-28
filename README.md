## Ansilbe Playbook to automate running of benchmarks

This playbook is for a research project related to performance benchmarking and is work in progress.
The repository is not stable yet and is only intended for known collaborators as of now.

### Installing ansible

We use ansible for benchmark automation.

	sudo pip install ansible

## Currently supported benchmarks/roles

Each benchmark is divided into it's own ansible role. You can apply these roles/benchmarks in the main.yml file.

There are other experimental non-benchmark roles like `kvm` and `vms` that are inteded for automating vm provisioning (but are not stable and entirely experimental, so please ignore these). Stable roles so far:

- geekbench

(Tested on ubuntu VM and container instances)

## What does each (benchmark) role do?

- Installs the benchmark(s)
- Runs the benchmark(s)
- Parses results to aggregate benchmark results and prints final relevant results to playbook stdout.

## Create inventory / host file
	
A sample inventory/hosts file is given along `sample_hosts`, however you can create your own inventory files. Currently we have 3 sections called `[baremetal]`, `[vms]` and `[containers]` in the inventory file for the root playbook files `site_baremetal.yml`, `site_vms.yml` and `site_containers.yml` respectively.

## Usage:

	# Running benchmark roles on [baremetal] entity(-es)
	ansible-playbook -i sample_hosts site_baremetal.yml

	# Running benchmark roles on [vms] (as defined in hosts file)
	ansible-playbook -i sample_hosts site_vms.yml

	# Running benchmark roles on [containers] (as defined in hosts file)
	ansible-playbook -i sample_hosts site_vms.yml
