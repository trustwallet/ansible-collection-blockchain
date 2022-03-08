import os
import pytest
import testinfra.utils.ansible_runner

from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# https://github.com/pytest-dev/pytest-testinfra/issues/345
# @pytest.fixture(scope='module')
# def ansible_vars(host):
#     defaults_files = "file=../../roles/cosmos/defaults/main.yml"
#     vars_files = "file=../../roles/cosmos/vars/%s.yml" % chain_name

#     host.ansible("setup")
#     host.ansible("include_vars", defaults_files)
#     host.ansible("include_vars", vars_files)
#     all_vars = host.ansible.get_variables()
#     all_vars["ansible_play_host_all"] = testinfra_hosts
#     templar = Templar(loader=DataLoader(), variables=all_vars)
    
#     return templar.template(all_vars, fail_on_undefined=False)

@pytest.mark.chain("osmosis")
def test_osmosisd_running_and_enabled(host):
    s = host.service('osmosisd')
    assert s.is_enabled

@pytest.mark.chain("terra")
def test_terrad_running_and_enabled(host):
    s = host.service('terrad')
    assert s.is_enabled
