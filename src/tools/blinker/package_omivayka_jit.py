#!/usr/bin/env python3
"""Package a built content_shell.app as an update to a TrollStore JIT build."""

import argparse
import os
from pathlib import Path
import plistlib
import re
import shutil
import subprocess
import tempfile
import zipfile


ICON_FILES = {
    "Omivayka60x60@2x.png": 120,
    "Omivayka60x60@3x.png": 180,
    "Omivayka76x76@2x.png": 152,
    "Omivayka83.5x83.5@2x.png": 167,
}
ENTITLEMENTS = {
    "com.apple.developer.kernel.extended-virtual-addressing": True,
    "com.apple.developer.kernel.increased-memory-limit": True,
    "get-task-allow": True,
}
RESOURCES = Path(__file__).resolve().parents[2] / "content/shell/app/ios/resources/artwork"


def read_installed_info(path):
    if path.suffix.lower() == ".plist":
        return plistlib.loads(path.read_bytes())
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist()
                   if re.fullmatch(r"Payload/[^/]+\.app/Info\.plist", name)]
        if len(members) != 1:
            raise ValueError("Expected one application Info.plist in the old package")
        return plistlib.loads(archive.read(members[0]))


def version(value, key):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]+(?:\.[0-9]+){0,2}", value):
        raise ValueError(f"Missing or invalid {key}: {value!r}")
    parts = tuple(map(int, value.split(".")))
    return parts + (0,) * (3 - len(parts))


def package(app, old_info, output, *, standalone=False):
    bundle_id = old_info.get("CFBundleIdentifier", "")
    if (not isinstance(bundle_id, str)
            or not re.fullmatch(r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", bundle_id)):
        raise ValueError("Expected the exact bundle ID of the installed browser")
    if "jit" not in bundle_id.split("."):
        raise ValueError("The installed browser is not a JIT build")
    if standalone:
        bundle_id = "com.wingto.omivayka.jit"

    info = plistlib.loads((app / "Info.plist").read_bytes())
    if info.get("CFBundleExecutable") != "content_shell":
        raise ValueError("Expected a built content_shell.app")
    for key in ("CFBundleVersion", "CFBundleShortVersionString"):
        if version(info.get(key), key) <= version(old_info.get(key), key):
            raise ValueError(f"The new {key} must exceed the installed value")
    minimum_os = version(info.get("MinimumOSVersion"), "MinimumOSVersion")
    if minimum_os != version(old_info.get("MinimumOSVersion"), "MinimumOSVersion"):
        raise ValueError("Build content_shell with the installed package's minimum iOS target")
    if output == app or app in output.parents:
        raise ValueError("The output directory must be outside the input app")
    build = subprocess.check_output(
        ["xcrun", "vtool", "-arch", "arm64", "-show-build", app / "content_shell"],
        text=True,
    )
    ios = re.search(r"^\s*platform IOS\s*\n\s*minos ([\d.]+)\s*$", build, re.M)
    if not ios:
        ios = re.search(r"^\s*cmd LC_VERSION_MIN_IPHONEOS\s*\n"
                        r"\s*cmdsize \d+\s*\n\s*version ([\d.]+)\s*$",
                        build, re.M)
    if not ios or version(ios[1], "deployment target") != minimum_os:
        raise ValueError("Expected a device arm64 executable with the app's minimum iOS target")

    output.mkdir(parents=True, exist_ok=True)
    suffix = "JIT Standalone" if standalone else "JIT"
    result = output / f"Omivayka Browser {info['CFBundleShortVersionString']} {suffix}.tipa"
    if result.exists():
        raise FileExistsError(result)
    with tempfile.TemporaryDirectory(dir=output) as scratch:
        work = Path(scratch)
        staged = work / "Payload/content_shell.app"
        shutil.copytree(app, staged, symlinks=True)
        for filename, size in ICON_FILES.items():
            subprocess.run(["sips", "-z", str(size), str(size),
                            RESOURCES / "omivayka-icon.png", "--out", staged / filename],
                           check=True, stdout=subprocess.DEVNULL)
        for scale in (1, 2, 3):
            suffix = f"@{scale}x" if scale > 1 else ""
            subprocess.run(["sips", "-z", str(120 * scale), str(120 * scale),
                            RESOURCES / "27367.png", "--out",
                            staged / f"blinker_logo{suffix}.png"],
                           check=True, stdout=subprocess.DEVNULL)

        info.update(CFBundleIdentifier=bundle_id,
                    CFBundleName="Omivayka Browser",
                    CFBundleDisplayName="Omivayka Browser",
                    CFBundleIcons={"CFBundlePrimaryIcon": {
                        "CFBundleIconFiles": ["Omivayka60x60"],
                    }})
        info["CFBundleIcons~ipad"] = {"CFBundlePrimaryIcon": {
            "CFBundleIconFiles": ["Omivayka60x60", "Omivayka76x76", "Omivayka83.5x83.5"],
        }}
        info.pop("CFBundleIconName", None)
        info.pop("CFBundleIconFile", None)
        (staged / "Info.plist").unlink()
        (staged / "Info.plist").write_bytes(plistlib.dumps(info))

        for framework in (staged / "Frameworks").glob("*.framework"):
            subprocess.run(["ldid", "-S", framework / framework.stem], check=True)
        entitlements = work / "entitlements.plist"
        entitlements.write_bytes(plistlib.dumps(ENTITLEMENTS))
        executable = staged / "content_shell"
        subprocess.run(["ldid", f"-S{entitlements}", executable], check=True)
        signed = plistlib.loads(subprocess.check_output(["ldid", "-e", executable]))
        if any(signed.get(key) != value for key, value in ENTITLEMENTS.items()):
            raise ValueError("Signed app does not contain the required entitlements")

        archive = work / "Omivayka Browser.tipa"
        subprocess.run(["zip", "-qry", archive, "Payload"], cwd=work, check=True)
        with zipfile.ZipFile(archive) as packaged:
            corrupt = packaged.testzip()
            if corrupt:
                raise ValueError(f"Corrupt archive member: {corrupt}")
        os.link(archive, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("app", type=Path, help="Built content_shell.app")
    parser.add_argument("installed", type=Path, help="Installed .tipa, .ipa or Info.plist")
    parser.add_argument("output", type=Path, help="Directory for the new .tipa")
    parser.add_argument("--standalone", action="store_true",
                        help="Use the independent Omivayka bundle identifier")
    args = parser.parse_args()
    try:
        result = package(args.app.resolve(), read_installed_info(args.installed),
                         args.output.resolve(), standalone=args.standalone)
    except (OSError, ValueError, subprocess.CalledProcessError,
            zipfile.BadZipFile, plistlib.InvalidFileException) as error:
        parser.exit(1, f"Packaging failed: {error}\n")
    print(result)


if __name__ == "__main__":
    main()
