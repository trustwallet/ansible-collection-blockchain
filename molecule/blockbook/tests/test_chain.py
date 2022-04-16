import os
import pytest
import testinfra.utils.ansible_runner

from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.chain("firo")
def test_blockbook_firo_running_and_enabled(host):
    s = host.service('blockbook-firo')
    assert s.is_enabled
    assert s.is_running

@pytest.mark.chain("firo")
def test_backend_firo_running_and_enabled(host):
    s = host.service('backend-firo')
    assert s.is_enabled
    assert s.is_running

@pytest.mark.chain("firo")
def test_http_is_listening(host):
    s = host.socket("tcp://0.0.0.0:9150")
    assert s.is_listening
