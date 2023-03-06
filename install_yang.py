import subprocess
import os

def run(cmd):
    print(f'run: "{cmd}"')
    proc = subprocess.run(
        cmd,
        shell=True,
        env=os.environ,
        capture_output=True,
    )
    output = []
    err = []
    for line in proc.stdout.decode().split("\n"):
        output.append(line)
        print(f"stdout: {line}")
    for line in proc.stderr.decode().split("\n"):
        err.append(line)
        print(f"stderr: {line}")
    ret = proc.returncode
    if ret != 0:
        raise Exception(f"{cmd} failed: ret: {ret}", ret, "".join(output), "".join(err))

    return "".join(output)

xlate_or = [
        "Device/org-openroadm-device",
        "Device/org-openroadm-ethernet-interfaces",
        "Device/org-openroadm-optical-tributary-signal-interfaces",
        "Device/org-openroadm-otn-odu-interfaces",
        "Device/org-openroadm-otn-otu-interfaces",
        "Device/org-openroadm-otsi-group-interfaces",
        "Common/org-openroadm-common-optical-channel-types",
        "Common/org-openroadm-common-types",
        "Common/org-openroadm-otn-common-types",
        "Common/org-openroadm-pm",
        "Common/org-openroadm-pm-types",
        "Common/org-openroadm-interfaces",
    ]

for m in xlate_or:
    run("sysrepoctl --search-dirs /home/OpenROADM_MSA_Public/model --install /home/OpenROADM_MSA_Public/model/" + m + ".yang")
