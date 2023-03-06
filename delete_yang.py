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
        "org-openroadm-device",
        "org-openroadm-ethernet-interfaces",
        "org-openroadm-optical-tributary-signal-interfaces",
        "org-openroadm-otn-odu-interfaces",
        "org-openroadm-otn-otu-interfaces",
        "org-openroadm-otsi-group-interfaces",
        "org-openroadm-common-optical-channel-types",
        "org-openroadm-common-types",
        "org-openroadm-otn-common-types",
        "org-openroadm-pm",
        "org-openroadm-pm-types",
        "org-openroadm-interfaces",
    ]

for m in xlate_or[::-1]:
    try:
        run("sysrepoctl --search-dirs /home/OpenROADM_MSA_Public/model --uninstall " + m)
    except Exception as e:
        print(str(e))
