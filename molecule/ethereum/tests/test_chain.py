import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_geth_is_installed(host):
    p = host.package('geth')
    assert p.is_installed

def test_gethd_running_and_enabled(host):
    s = host.service('gethd')
    assert s.is_enabled
    assert s.is_running

def test_http_is_listening(host):
    s = host.socket("tcp://0.0.0.0:8545")
    assert s.is_listening