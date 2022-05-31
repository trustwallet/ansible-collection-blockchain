# Nano Role

Ansible role to manage Nano blockchain node.

## Role Variables

The role has default variables (see `defaults/main.yml`) which can be adjusted.

## Example Playbook

```yaml
- hosts: "all"
  gather_facts: true

  roles:
    - role: geerlingguy.docker # for nano_node
      become: true
    - role: gantsign.golang # for nano_rpc_cache
      golang_version: "1.18.1"
      golang_install_dir: /usr/local/go


    - role: trustwallet.blockchain.nano
      data_dir: /mnt/data/nano # exampe of non-default data directory, default is /home/nano/.nano
      nano_node: true # default, could be omitted
      nano_work_server: true # default, could be omitted
      nano_work_server_peers: # default, could be omitted
        - http://localhost:7776
      nano_work_server: true # default, Work Generation needs a machine with GPU attached
```

Nano documentation suggests to split RPC node and Work Generation to separate machines, but single setup machine still valid.

Alternative setup with two machines:

```yaml
- hosts: "nano_node"
  gather_facts: true

  roles:
    - role: geerlingguy.docker # for nano_node
      become: true
    - role: gantsign.golang # for nano_rpc_cache
      golang_version: "1.18.1"
      golang_install_dir: /usr/local/go

    - role: trustwallet.blockchain.nano
      data_dir: /mnt/data/.nano # exampe of non-default data directory, default is /home/nano/.nano
      nano_node: true
      nano_work_server: false
      nano_work_server_peers: # note: only a single worker server peer is supported atm
        - https://<work-server-ip>:7776

- hosts: "nano_work_server"
  gather_facts: true
  
  roles:
    - role: trustwallet.blockchain.nano
      nano_node: false
      nano_work_server: true
```

## Popular Questions

### Hardware Recommendations

Non-voting and Representative Nodes:

* 8GB RAM
* Quad-Core CPU
* 250 Mbps bandwidth (4TB or more of available monthly bandwidth)
* SSD-based hard drive with 400GB+ of free space

For nodes being used with services requiring regular or high volume sending and receiving of transactions,
special considerations must be made for handling Proof-of-Work generation activities.
See [Work Generation](https://docs.nano.org/integration-guides/work-generation/) guidance.

### Port Configuration

* `7075` - Nano P2P port for the node to participate on the network, should be open to the world `0.0.0.0/0`.

* `7076` - Nano RPC access port, should only be available to those you wish to have control of the node, since option to `enable_control` is set to on.

* `7176` - [Nano RPC Cache](https://github.com/catenocrypt/nano-work-cache) is an additional caching layer (not official), which simplifies interaction for
light wallets which need to perform work generation on the server side,
provides cache for some actions, and blocks potentially risky actions from being invoked outside of the local peers, should be open to the world `0.0.0.0/0`.

* `7776` - Nano Worker Server port, so Nano PRC can request work generation.

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

```shell
molecule -v test -s nano
```

## References

* [Trust Wallet](https://trustwallet.com)
* [Nano GitHub](https://github.com/nanocurrency/nano-node)
* [Nano Documentation](https://docs.nano.org/running-a-node/overview/)
* [Nano RPC commands](https://docs.nano.org/commands/rpc-protocol/)
* [Nano Troubleshooting](https://docs.nano.org/running-a-node/troubleshooting/)

## License

MIT
