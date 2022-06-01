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
    - role: nvidia.nvidia_driver # for nano-work-server
      become: true

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
    - role: nvidia.nvidia_driver # for nano-work-server
      become: true

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

NOTE: ARM based platforms is not yet supported for Nano Work Server.

NOTE: This role doesn't install any GPU drivers, should be installed separately (examples shows the NVIDIA driver installation).

### Port Configuration

* `7075` - Nano P2P port for the node to participate on the network, should be open to the world `0.0.0.0/0`.

* `7076` - Nano RPC access port, should only be available to those you wish to have control of the node, since option to `enable_control` is set to on.

* `7376` - [Nano RPC Cache](https://github.com/catenocrypt/nano-work-cache) is an additional caching layer (not official), which simplifies interaction for
light wallets which need to perform work generation on the server side,
provides cache for some actions, and blocks potentially risky actions from being invoked outside of the local peers, should be open to the world `0.0.0.0/0`.

* `7176` - Nano Worker Server port, so Nano PRC can request work generation.

## Troubleshooting

### nano-work-server – Unable to get platform id list after 10 seconds of waiting.

 🔰 **Ensure drivers are installed correctly**

On Linux you can check with the `sudo lshw -C display` command.  

<details>
<summary>Example output</summary>

```sh
$ sudo lshw -C display
  *-display:0 UNCLAIMED     
      description: VGA compatible controller
      product: GD 5446
      vendor: Cirrus Logic
      physical id: 2
      bus info: pci@0000:00:02.0
      version: 00
      width: 32 bits
      clock: 33MHz
      capabilities: vga_controller
      configuration: latency=0
      resources: memory:e8000000-e9ffffff memory:ee080000-ee080fff memory:c0000-dffff
  *-display:1
      description: VGA compatible controller
      product: GK104GL [GRID K520]
      vendor: NVIDIA Corporation
      physical id: 3
      bus info: pci@0000:00:03.0
      version: a1
      width: 64 bits
      clock: 33MHz
      capabilities: pm msi pciexpress vga_controller bus_master cap_list rom
      configuration: driver=nvidia latency=248
      resources: irq:114 memory:ec000000-ecffffff memory:e0000000-e7ffffff    memory:ea000000-ebffffff ioport:c100(size=128) memory:ee000000-ee07ffff
```
</details>

Should be no `UNCLAIMED` next to the target GPU device (in the example NVIDIA GRID K520 card has drivers installed correctly).

🔰 **Which type of driver do I need?**

It really depends on the system specification and goes far beyond this Ansible role. But in our tests and working environment we are running on AWS `g5.2xlarge` GPU Accelerated instances with NVIDIA GRID K520 GPUs. The working driver for this graphics card can be installed with Ansible role:

```yml
  roles:
    - role: nvidia.nvidia_driver
      nvidia_driver_branch: 470 # not the latest, since latest 510 branch not working
```

🔰 **Driver is fine, but doesn't work**

As it says in [nano-work-server](https://github.com/nanocurrency/nano-work-server) project, if the OpenCL library cannot be found in the PATH, it may be necessary to link against explicitly. It can be done by passing the `opencl_lib_path` variable.

```yml
  roles:
    - role: trustwallet.blockchain.nano
      opencl_lib_path: "/path/to/opencl.lib"
```

🔰 **ARM based platform? Not yet supported for Nano Work Server**

There is an open [issue](https://github.com/nanocurrency/nano-work-server/issues/33) at the project GitHub.

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
* [Nano RPC Cache](https://github.com/catenocrypt/nano-work-cache)
* [Nano Work Server](https://github.com/nanocurrency/nano-work-server)

## License

MIT
