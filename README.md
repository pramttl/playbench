## Ansilbe Playbook to automate running of benchmarks

Playbench is a tool (ansible playbook + other scripts) to facilitate and automate performance benchmarking in the data center. The current project is a prototype and not stable yet. It is primarily intended for known collaborators. The goal of playbench is to be a benchmark automation tool.

Amongst the problems Playbench aims at solving, few of the key ones are:

* Eliminating the need to manually install each benchmark and its package dependencies.
* Spawning same benchmark on multiple nodes.
* Syncrhonizing the start of the benchmark on multiple nodes.
* Parsing final results from each node / virtual entity (VM, docker containers, etc) being benchmarked and aggregating results to stdout at the control node. (requires benchmark specific parsing logic)
* Allowing the same benchmark to be used on both VMs and docker containers.
* Evaluating performance of each node or virtual entity in the inventory.

### Installing ansible

Ansible is required to use Playbench as playbench is primarily modelled as an ansible playbook.

	sudo pip install ansible

## Currently supported benchmarks/roles

One of key ideas behind Playbench is to have each benchmark modelled as a separate ansible role. This way, it is possible to apply these modular roles (benchmarks), to any inventory of nodes - hardware/virtual machines/containers of choice.

There are other experimental non-benchmark roles like `kvm` and `vms` that are inteded for automating vm provisioning (but are not stable and entirely experimental, so please ignore these). Supported benchmarks so far:

- geekbench (stable, tested on Ubuntu 14.04)
- fio (partly stable)

## What should each benchmark/role do?

Each benchmark/role at min must do the following:

- Install the benchmark(s) and it's dependencies.
- Run the benchmark(s)
- Parse benchmark output on each node, collecting relevant metrics and and printing final results to playbook stdout.

Benchmark / Role specific features are described below:

#### Role: Geekbench

The final output of this role which is printed out by ansible debug are 17 values:

```
num_hosts  # num of hosts on which benchmark ran
single-core-score
multi-core-score
single-core-integer
multi-core-integer
single-core-floating
multi-core-floating
single-core-memory
multi-core-memory
stream-copy-single-core
stream-copy-multi-core
stream-scale-single-core
stream-scale-multi-core
stream-add-single-core
stream-add-multi-core
stream-triad-single-core
stream-triad-multi-core
```

(Tested on ubuntu VM and container instances)

Todo: Other roles are yet to be documented.

## Creating an inventory / host file

An inventory file is used to list all the nodes or virtual entities on which a benchmark (role) is to be applied.

A sample inventory/hosts file is given along `sample_hosts`, however you can create your own inventory files. Currently we have 3 sections called `[baremetal]`, `[vms]` and `[containers]` in the inventory file for the root playbook files `site_baremetal.yml`, `site_vms.yml` and `site_containers.yml` respectively.

## Usage:

	# Running benchmark roles on [baremetal] entity(-es)
	ansible-playbook -i sample_hosts site_baremetal.yml

	# Running benchmark roles on [vms] (as defined in hosts file)
	ansible-playbook -i sample_hosts site_vms.yml

	# Running benchmark roles on [containers] (as defined in hosts file)
	ansible-playbook -i sample_hosts site_vms.yml

## Creating VMs
 
You can create VMs whichever way you like and add to hosts file. The only requirement is that the VMs should have networking enabled. Some roles require fetching packages so public networking on the VMs is required for most of the benchmarks / roles.

## Creating docker containers

The following command will pull in a bare-bones ubuntu container with python installed so that it can be configured via ansible. (All hosts that can be configured with ansible require python running on them. Note that, you can also use your own container(s) as long as they have python installed on them)

	docker pull pramttl/ubuntu-python

	# Start a container with the pulled image
	docker run -it pramttl/ubuntu-python

	# Press Ctrl+p Ctrl+q, to exit container shell and keep it running in background


## Suggestions

If you would like to see a benchmark included in Playbench that is not supported yet please send an email to `mittalp<at>oregonstate<dot>edu`, with the name of the benchmark and supporting details. Any other suggestions are also very welcome.