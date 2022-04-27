# Polygon Role

Ansible role to manage Polygon blockchain node.

The role is based on the original [Polygon Ansible playbook](https://github.com/maticnetwork/node-ansible),
but contains automatic snapshot sync.

NOTE: The role currently sets up only the Full RPC node.
To set up the `sentry/validator` node feel free
to follow the original instruction or submit a Pull Request.

## Requirements

### Golang

This role doesn't attempt to install the golang, but assumes it is available
at the default location `/usr/local/go/bin`. The default location can be overridden
with the `golang_bin_dir` variable when executing the role.

Tip: Golang can be installed with Ansible Galaxy [gantsign.golang](https://galaxy.ansible.com/gantsign/golang) role or similar.


## Role Variables

The role has default variables (see `defaults/main.yml`) which can be adjusted.

## Example Playbook

```yaml
- hosts: "all"
  gather_facts: true
  become: true
  
  roles:
    - role: gantsign.golang
      golang_version: "1.18.1"
      golang_install_dir: /usr/local/go

    - role: trustwallet.blockchain.polygon
      data_dir: /mnt/data # exampe of non-default data directory, default is /home/polygon
      quicksync_mode: full # options are archive, full, pruned and none (sync bor from scratch)
      bor_config:
        HTTPModules:
          - eth
          - net
          - web3
          - txpool
          - bor
```

## Popular Questions

### What ports does Polygon blockchain node use?

The sentry machine must have the following ports open:

* `26656` - Heimdall P2P port to connect the node to other nodes, should be open to the world `0.0.0.0/0`.

* `26657` - Heimdall RPC port, should not be exposed to the world.

* `1317` - Heimdall REST API port, will be used by Bor.

* `30303` - Bor P2P port to connect the node to other nodes,should be open to the world `0.0.0.0/0`.

* `8545` - Bor RPC port (used for HTTP API and websocket).

* `22` - For the validator to be able to ssh open to the specific subnet where Validator is configured.


### What are the sizes of Polygon Chains Snapshots?

* Mainnet Archive Bor snapshot ~10TiB
* Mainnet FullNode Bor snapshot ~870GiB
* Mainnet Pruned Bor snapshot ~700GiB
* Mainnet Heimdall snapshot ~130GiB

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

```shell
molecule -v test -s polygon
```

## References

* [Trust Wallet](https://trustwallet.com)
* [Original Polygon Full Node Deployment with Ansible](https://docs.polygon.technology/docs/develop/network-details/full-node-deployment/)
* [Polygon Chains Snapshots](https://snapshots.matic.today/)
* [Snapshot Instructions for Heimdall and Bor](https://forum.matic.network/t/snapshot-instructions-for-heimdall-and-bor/2278)
* Alternatively, [Run Polygon node with Docker](https://chasewright.com/how-to-run-a-polygon-matic-mainnet-node/)

## License

MIT
