import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_heimdall_running_and_enabled(host):
    s = host.service('heimdalld')
    assert s.is_running
    assert s.is_enabled

def test_heimdalld_p2p_is_listening(host):
    s = host.socket("tcp://0.0.0.0:26656")
    assert s.is_listening

def test_heimdall_rest_server_running_and_enabled(host):
    s = host.service('heimdalld-rest-server')
    assert s.is_running
    assert s.is_enabled

def test_heimdalld_rest_server_is_listening(host):
    s = host.socket("tcp://0.0.0.0:1317")
    assert s.is_listening

def test_bor_running_and_enabled(host):
    s = host.service('bor')
    assert s.is_running
    assert s.is_enabled

def test_bor_p2p_is_listening(host):
    s = host.socket("tcp://0.0.0.0:30303")
    assert s.is_listening

def test_bor_rpc_is_listening(host):
    s = host.socket("tcp://0.0.0.0:8545")
    assert s.is_listening
