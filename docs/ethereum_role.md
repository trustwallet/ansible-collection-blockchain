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
      data_dir: /mnt/data # example of custom data dir, default is /home/users/.ethereum
      geth_config:
        Eth:
          SyncMode: full
```

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
