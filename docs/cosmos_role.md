# Cosmos Role

Ansible role to manage Cosmos-SDK based blockchain nodes.

## Requirements

The Cosmos-SDK based chains are distributed for may operating systems.
Check the project's GitHub repository to see if it releases binary for the
operating system of your choice. But this role only targeting the Linux/Unix 
based OS.

### Golang

This role doesn't attempt to install the golang, but assumes it is available
at the default location `/usr/local/go/bin`. If in your system golang is installed 
to other directory, override the `golang_bin_dir` variable when executing the role.

Golang can be installed with Ansible Galaxy (gantsign.golang)[https://galaxy.ansible.com/gantsign/golang] role.

## Role Variables

The role applies variables specified in the `defaults/main.yml` to `config.toml`
and `app.toml` configuration files.

The execution command is the following:

```shell
{{ bin_dir }}/cosmovisor start --home {{ chain_data_dir }} {{ chain_bin_flags }}
```

Also, Cosmos-SDK based chains might have their own variables file
(e.g. `vars/osmosis.yml`) to override some config variables.

The general rule here, if it makes sense to have the missed parameter configurable,
then submit a pull request to add the flag to `defaults/main.yml` or 
`vars/<chain>.yml` for specific chain overrides, and modify `tasks/config.yml` or
`tasks/config_<chain>.yml` to apply the introduced variable.

Some Comsmos-SDK based chains accept additional parameters as command-line flags.
These flags can be specified via `chain_bin_flags` variable. F.e. `terrad` suggests
`--x-crisis-skip-assert-invariants` flag to start syncing the node since the last upgrade until it is at the current height (we have alrteady set this variable in `vars/terra.yml`).

## Example Playbook

```yaml
- import_role:
    name: trustwallet.blockchains.cosmos
  vars:
    ansible_become: true
    chain_name: osmosis
    chain_data_dir: /mnt/data/.osmosisd
    quicksync_mode: default
    quicksync_mirror: SanFrancisco
    quicksync_tmp_dir: /tmp/sync
```

_When Ansible Role targeting an AWS EC2 insance, it might be a good idea to
change the `chain_data_dir` to target directory at attached & mounted 
EBS volume (and ensure the EBS Volume is retained on EC2 Instance termination).
Attaching and mounting the AWS EBS volume is out of scope of this role._

## Popular Questions

### What ports does Cosmos-SDK based chain node use?

By default chain's binary uses the following ports:

* `26656` - p2p networking port to connect to the tendermint network
  On a validator this port needs to be exposed to sentry nodes
  On a sentry node this port needs to be exposed to the open internet

* `26657` - Tendermint RPC port
  This should be shielded from the open internet

* `26658` - Out of process ABCI app
  This should be shielded from the open internet

* `26660` - Prometheus stats server
  Stats about the gaiad process
  Needs to be enabled in the config file .
  This should be shielded from the open internet

* `1317` - Light Client Daemon
  For automated management of anything you can do with the CLI
  This should be shielded from the open internet, unless public sentry node is planned.

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

The role to test the Cosmos-SDK based chains, expects the `COSMOS_CHAIN_NAME` parameter
to be set as environment variable.

```shell
COSMOS_CHAIN_NAME=osmosis molecule -v test -s cosmos
```

## References

* [Trust Wallet](https://trustwallet.com)
* [Cosmos SDK](https://v1.cosmos.network/sdk)
* [Cosmos-SDK based chains registry](https://github.com/cosmos/chain-registry/)

## License

MIT
