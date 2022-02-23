# Ethereum Role

Ansible role to manage Ethereum blockchain node with Geth.

## Requirements

The `geth` can be launched on many operating systems, but this role at the moment only targeting Linux/Unix based operating systems.

## Role Variables

The role has default geth configuration (see `defaults/main.yml`) combined with the `geth_config` override passed as a role parameter.

Geth variables could also be configured by specifying `extra_run_args` variable
when executing the role.

The execution command is the following:

```shell
{{ chain_bin }} --config {{ chain_config_dir }}/config.toml {{ extra_run_args }}
```

## Example Playbook

```yaml
- hosts: "all"
  gather_facts: true
  become: true
  
  roles:
    - role: trustwallet.blockchain.ethereum
      chain_data_dir: /mnt/data
      geth_config:
        Eth:
          SyncMode: full
```

_When Ansible Role targeting an AWS EC2 instance, it might be a good idea to
change the `chain_data_dir` to target directory at attached & mounted 
EBS volume (and ensure the EBS Volume is retained on EC2 Instance termination).
Attaching and mounting the AWS EBS volume is out of scope of this role._

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

```shell
molecule -v test -s ethereum
```

## References

* [Trust Wallet](https://trustwallet.com)
* [Go Ethereum (geth)](https://geth.ethereum.org/)

## License

MIT
