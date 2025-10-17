BASH: str = "bash"
ETHTOOL: str = "ethtool"
IP: str = "ip"
MOUNT: str = "mount"
NFTABLES: str = "nft"
OVS_VSCTL: str = "ovs-vsctl"
SYSCTL: str = "sysctl"
TC: str = "tc"
TEST: str = "test"
UMOUNT: str = "umount"
VCMD: str = "vcmd"
VNODED: str = "vnoded"
NSENTER: str = "nsenter"
MKNODE: str = "core-mknode"

COMMON_REQUIREMENTS: list[str] = [
    BASH,
    ETHTOOL,
    IP,
    MOUNT,
    NFTABLES,
    SYSCTL,
    TC,
    TEST,
    UMOUNT,
    VCMD,
    VNODED,
]
OVS_REQUIREMENTS: list[str] = [OVS_VSCTL]


def get_requirements(use_ovs: bool, use_unshare: bool) -> list[str]:
    """
    Retrieve executable requirements needed to run CORE.

    :param use_ovs: True if OVS is being used, False otherwise
    :param use_unshare: True if unshare/nsenter is used for nodes, False otherwise
    :return: list of executable requirements
    """
    requirements = COMMON_REQUIREMENTS
    if use_ovs:
        requirements += OVS_REQUIREMENTS
    if use_unshare:
        requirements += [MKNODE, NSENTER]
    return requirements
