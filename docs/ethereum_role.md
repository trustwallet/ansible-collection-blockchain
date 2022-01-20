# Ethereum Role

Ansible role to manage Ethereum blockchain node with Geth.

## Requirements

The `geth` can be launched on many operating systems, but this role only targeting `Ubuntu` distribution.

## Role Variables

This roles is using the dumped on-the-fly `geth` config and set
parameters specified in `defaults/main.yml`.
For cases when certain parameter is not available for override,
the `chain_bin_flags` variable can accept any geth command-line flags.
The execution command is the following:

```
{{ chain_bin }} --config {{ chain_config_path }} {{ chain_bin_flags }}
```

The general rule here, if it make sense to have the chosen parameter appear in `config.toml` for better clarity, then submit a pull request to add the flag to `defaults/main.yml`; otherwise pass the additional configuration via `chain_bin_flags`

See the deaults/main.yml to find role defaults.

One of the parameters that can be override is `chain_data_dir`, is the 
data directory for the config, databases and keystore.

### Geth Variables

| Parameter | Choices/Defaults | Comments | 
| geth_syncmode | `snap` | Blockchain sync mode ("fast", "full", "snap" or "light") |
| geth_http | `true` | Enable the HTTP-RPC server |
| geth_http_addr | `0.0.0.0` | HTTP-RPC server listening interface |
| geth_http_port | `8545` | HTTP-RPC server listening port |
| geth_http_api | `eth,net,web3` | API's offered over the HTTP-RPC interface |
| geth_http_vhosts | `*` | Comma separated list of virtual hostnames from which to accept requests (server enforced). Accepts '*' wildcard. |
| geth_metrics | `true` | Enable metrics collection and reporting |
| geth_metrics_addr | `0.0.0.0` | Enable stand-alone metrics HTTP server listening interface |
| geth_metrics_port | `6060` | Metrics HTTP server listening port |


## Example Playbook

```yml
- hosts: servers
  roles:
    - role: trustwallet.blockchains.ethereum
      become: yes
      geth_datadir: /mnt/data

# or
- hosts: servers
  taks:
    - import_role:
        name: trustwallet.blockchains.ethereum
      vars:
        ansible_become: yes
        geth_datadir: /mnt/data
```



_When Ansible Role targeting an AWS EC2 insance, it might be a good idea to
change the `geth_datadir` to target directory at attached and mounted 
EBS volume (and ensure the EBS Volume is retained on EC2 Instance termination).
Attaching and mounting the AWS EBS volume is out of scope of this role._


## License

MIT

## Author Information

[Trust Wallet](https://trustwallet.com)
