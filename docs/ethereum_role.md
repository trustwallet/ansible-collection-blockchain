# Ethereum Role

Ansible role to manage Ethereum blockchain node with Geth.

## Requirements

The `geth` can be launched on many operating systems, but this role only targeting Linux/Unix based operating systems.

## Role Variables

The role is using the dumped on-the-fly `geth` config and applies the
variables specified in `defaults/main.yml`. 
Check the `defaults/main.yml` to see the parameters available for override
and their role default variables. Other variables not listed there have 
the defaults according to `geth` documentation, and can be changed
by specifying `chain_bin_flags` variable when executing the role. 

The execution command is the following:

```shell
{{ chain_bin }} --config {{ chain_config_path }} {{ chain_bin_flags }}
```

The general rule here, if it make sense to have the missed parameter
configurable, then submit a pull request to add the variable
to `defaults/main.yml`, and modify `tasks/config.yml`; otherwise pass the
additional configuration via `chain_bin_flags`.

One of the parameters that can be overriden is `chain_data_dir`, the 
data directory for the config, databases and keystore.

## Example Playbook

```yaml
- hosts: servers
  taks:
    - import_role:
        name: trustwallet.blockchains.ethereum
      vars:
        ansible_become: yes
        chain_data_dir: /mnt/data
```

_When Ansible Role targeting an AWS EC2 insance, it might be a good idea to
change the `chain_data_dir` to target directory at attached & mounted 
EBS volume (and ensure the EBS Volume is retained on EC2 Instance termination).
Attaching and mounting the AWS EBS volume is out of scope of this role._

## References

* [Trust Wallet](https://trustwallet.com)
* [Go Ethereum (geth)](https://geth.ethereum.org/)

## License

MIT
