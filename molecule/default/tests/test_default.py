"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_user_exists(host):
    """Verify that the devops user exists."""
    assert host.user("devops").name == "devops"


def test_ssh_config_exists(host):
    """Verify that the devops sudo config file exists."""
    f = host.file("/etc/sudoers.d/devops")
    assert f.exists
    assert f.is_file


def test_sudo_config(host):
    """Verify that the devops user can run any command via sudo."""
    with host.sudo("devops"):
        cmd = host.run("sudo ls")
        assert cmd.succeeded
