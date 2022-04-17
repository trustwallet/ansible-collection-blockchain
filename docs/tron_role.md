# TRON role

Ansible role to manage TRON blockchain node.

## Requirements

The TRON blockchain Java Archive can be launched on many operating systems.
Check the project's GitHub repository to see the instructions for the
operating system of your choice. But this role only targeting the Linux/Unix 
based OS.

### JDK 8

This role requires the compatible Java runtime to be installed and assume it is present in the system.
We've found that Amazon Corretto, production-ready distribution of OpenJDK, does the job well.

Tip: JDK can be installed with Ansible Galaxy [lean_delivery.java](https://galaxy.ansible.com/lean_delivery/java) role or similar.

## Role Variables

The role has default variables (see `defaults/main.yml`) which can be adjusted.

## Example Playbook

By default, the role will use the [main_net_config.conf](https://github.com/tronprotocol/tron-deployment/blob/master/main_net_config.conf).
But it can be replaced with the custom config.

```yaml
- hosts: "all"
  gather_facts: true
  become: true
  
  roles:
    - role: lean_delivery.java
      java_distribution: corretto
      java_major_version: 8

    - role: trustwallet.blockchain.tron
      data_dir: /mnt/data # exampe of non-default data directory, default is /home/tron/.tron
      quicksync_mirror: oregon # options are oregon (default), frankfurt and singapore
      tron_config_override: ./config/main_net_config.conf # optional, set up a nodes with a new custom cofnig file
```

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

```shell
molecule -v test -s tron
```


## References

* [Trust Wallet](https://trustwallet.com)
* [TRON GitHub](https://github.com/tronprotocol/java-tron)
* [TRON Full Node Deployment](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode)
* [TRON Full Node API](https://developers.tron.network/reference/full-node-api-overview)

## License

MIT
