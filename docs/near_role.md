# NEAR Role

Ansible role to manage NEAR blockchain node.

The role installs Rust to compile NEAR binary. The compilation takes very long, be patient.

## Role Variables

The role has default variables (see `defaults/main.yml`) which can be adjusted.

## Example Playbook

```yaml
- hosts: "all"
  gather_facts: true
  become: true
  
  roles:
    - role: trustwallet.blockchain.near
      near_home_dir: /mnt/data/.near
      quicksync_mode: rpc
```

_When Ansible Role targeting an AWS EC2 instance, it might be a good idea to
change the `near_home_dir` to target directory at attached & mounted 
EBS volume (and ensure the EBS Volume is retained on EC2 Instance termination).
Attaching and mounting the AWS EBS volume is out of scope of this role._

## Development

To aid in the development and testing of the Ansible role, we are 
using [Molecule](https://molecule.readthedocs.io/en/latest/index.html) roles testing framework.

```shell
molecule -v test -s near
```

## References

* [Trust Wallet](https://trustwallet.com)
* [NEAR GitHub](https://github.com/near/nearcore)
* [NEAR Docs](https://docs.near.org/docs/develop/node/intro/what-is-a-node)

## License

MIT
