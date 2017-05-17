from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_transmission(host):
    service = host.service('transmission-daemon')
    assert service.is_running
    assert service.is_enabled
