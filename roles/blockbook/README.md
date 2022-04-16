# Blockbook Role

Ansible role to manage [Blockbook](https://github.com/trezor/blockbook) supported blockchains.

## Requirements

Officially supported platform is Debian Linux and AMD64 architecture.

### Docker CE

This role doesn't attempt to install the Docker CE, but assumes it is available.

Tip: Docker can be installed with Ansible Galaxy (geerlingguy.docker)[https://galaxy.ansible.com/geerlingguy/docker] role or similar.

## Role Variables

The role has default variables (see `defaults/main.yml`) which can be adjusted.

## Example Playbook

```yaml
---
- hosts: "all"
  gather_facts: true
  become: true
  remote_user: admin

  roles:
    - role: geerlingguy.docker

    - role: trustwallet.blockchain.blockbook
      chain_name: firo
      data_dir: /mnt/data/ # example of custom data_dir, default is /root
```

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

The role to test the Blockbook supported blockchains expects the `BLOCKBOOK_CHAIN_NAME` parameter
to be set as environment variable.

```shell
BLOCKBOOK_CHAIN_NAME=firo molecule -v test -s blockbook
```

## References

* [Trust Wallet](https://trustwallet.com)
* [Blockbook](https://github.com/trezor/blockbook)

## License

MIT
