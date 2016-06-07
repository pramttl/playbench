## Ansilbe Playbook to automate running of benchmarks

This playbook is for a research project related to performance benchmarking and is work in progress.
The repository is not stable yet and is only intended for known collaborators as of now.

## Currently supported benchmarks/roles

Each benchmark is divided into it's own ansible role. You can apply these roles/benchmarks in the main.yml file.

- Geekbench

## What does this playbook do?

- Todo: Automatically spawn KVM/QEMU virtual machines before running benchmarks
- Todo: Automatically spawn docker containers before running benchmarks
- Installs benchmarks
- Runs the benchmarks

## Create inventory / host file
	
Create an inventory file called `hosts` at the root level of this directory with the following section:

	[baremetal]
	<baremetal_node_ip>

## Usage:

	ansible-playbook -i hosts main.yml
