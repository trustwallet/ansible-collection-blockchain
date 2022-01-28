# Ansible Collection - trustwallet.blockchains

Trust Wallet is a most trusted & secure crypto wallet.

The Ansible Collection contains Trust Wallet's roles to manage blockchain nodes.

List of the collection roles:

* `trustwallet.blockchains.cosmos` - All Cosmos-SDK based chains
* `trustwallet.blockchains.ethereum` - Go Ethereum (geth)
* _...more are coming_

## Ansible Collection Usage

Install the collection using the following command:

```shell
ansible-galaxy collection install trustwallet.blockchains
```

Example setting up Ethereum Full Node with the collection role:

```yaml
# playbook.yml
---
- hosts: "all"
  gather_facts: true
  
  pre_tasks:
    - name: "Install apt packages"
      ansible.builtin.apt:
        update_cache: yes
        pkg:
          - python3
          - python3-pip
          - python3-setuptools

  tasks:
    - import_role:
        name: trustwallet.blockchains.ethereum
      vars:
        ansible_become: true
        chain_data_dir: /mnt/data
        geth_syncmode: full
        geth_metrics: false
```

## Contributing

The best way to submit feedback and report bugs is to [open a GitHub issue](https://github.com/trustwallet/ansible-collection-blockchains/issues).

## Development

### Molecule Testing Framework

Development/integration of the roles are configured with Molecule and EC2 driver.

It's recommended to develop inside [Virtual environment](https://virtualenv.pypa.io/en/latest/)

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r molecule/requirements.txt
```

Provide AWS credentials to allow Molecule provision ephemeral EC2 instance.

```shell
export AWS_PROFILE=
# or 
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_KEY=
```

Also provide the target region, image AMI and VPC subnet identifier

```shell
export AWS_REGION=us-east-1
export MOLECULE_VPC_SUBNET_ID=subnet-...
export MOLECULE_IMAGE=ami-...
```

For each role there is a `/molecule/<role>` directory with configuration files.

Execute full integration scenario which includes steps to install all dependencies, create EC2 instance, execute role, test, cleanup and finally destroy EC2 instance run the following command (e.g. `ethereum` role).

```shell
molecule test -s ethereum
```

Or launch instance and execute a role

```shell
molecule converge -s ethereum
```

And verify

```shell
molecule verify -s ethereum
```

Jump to the node

```shell
molecule login -s ethereum
```

Finally, cleanup and destroy

```shell
molecule destroy -s ethereum
```

### Build Ansible Galaxy Locally

To build the local version of the Ansible Galaxy collection:

```sh
ansible-galaxy collection build --force
```

The `trustwallet-blockchains-x.x.x.tar.gz` file will appear at the root of the project.

It can be installed for local testing by executing the following command:

```sh
ansible-galaxy collection install trustwallet-blockchains-0.1.0.tar.gz --force
```

## References

* [Trust Wallet](https://trustwallet.com) crypto wallet project page
* [Trust Wallet Collection](https://galaxy.ansible.com/trustwallet/blockchains) Ansible Galaxy page
* [Molecule](https://molecule.readthedocs.io/en/latest/index.html) Ansible roles testing framework
* [Testinfra](https://testinfra.readthedocs.io/en/latest/) unit tests in Python to test actual state of the server configured by Ansible/Molecule

## License

Ansible Collection `trustwallet.blockchains` is available under the [MIT](LICENSE) license.
