import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nano_rpc_cache_running_and_enabled(host):
    s = host.service('nano-rpc-cache')
    assert s.is_enabled
    assert s.is_running

def test_nano_work_server_running_and_enabled(host):
    s = host.service('nano-work-server')
    assert s.is_enabled
    assert s.is_running

def test_nano_p2p_is_listening(host):
    s = host.socket("tcp://0.0.0.0:7075")
    assert s.is_listening

def test_nano_rpc_is_listening(host):
    s = host.socket("tcp://0.0.0.0:7076")
    assert s.is_listening

def test_nano_rpc_cache_is_listening(host):
    s = host.socket("tcp://0.0.0.0:7376")
    assert s.is_listening

def test_nano_work_server_is_listening(host):
    s = host.socket("tcp://0.0.0.0:7176")
    assert s.is_listening
