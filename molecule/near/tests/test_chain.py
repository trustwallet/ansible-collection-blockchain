import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_neard_running_and_enabled(host):
    s = host.service('neard')
    assert s.is_running
    assert s.is_enabled

def test_http_is_listening(host):
    s = host.socket("tcp://0.0.0.0:3030")
    assert s.is_listening
