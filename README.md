# Ansible Collection - trustwallet.blockchains

Trust Wallet is a most trusted & secure crypto wallet.

The Ansible Collection contains Trust Wallet's roles to manage blockchain nodes.


## Ansible Collection Usage

Install the collection using the following command:

```shell
ansible-galaxy collection install trustwallet.blockchains
```

## Contributing

The best way to submit feedback and report bugs is to [open a GitHub issue](https://github.com/trustwallet/ansible-collection-blockchains/issues).

## Development

Development/integration of the roles are configured with Molecule and EC2 driver.

It's recommended to develop inside [Virtual environment](https://virtualenv.pypa.io/en/latest/)

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r ./molecule/requirements
```

Provide AWS credentials to allow Molecule provision ephemeral EC2 instance.

```shell
export AWS_PROFILE=
# or 
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_KEY=
```

Also provide the target region and VPC subnet identifier

```shell
export AWS_REGION=us-east-1
export VPC_SUBNET_ID=subnet-...
```

For each role there is a `/molecule/<role>` directory with configration files.

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

### References

* [Testinfra](https://testinfra.readthedocs.io/en/latest/) unit tests in Python to test actual state of the server configured by Ansible/Molecule.

## License

Ansible Collection `trustwallet.blockchains` is available under the [MIT](LICENSE) license.