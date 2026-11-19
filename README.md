<p align="center">
  <img width="100" height="100" alt="Blinker Fluid" src="https://github.com/user-attachments/assets/67a507ac-e528-4720-abd8-23930b242dc0" />
</p>

<h1 align="center">Blinker Fluid</h1>

<p align="center">
  <strong>An experimental Chromium Blink + V8 browser for iOS.</strong><br>
  Runs without Apple's WebKit engine.
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v.0.3.1-blue">
  <img alt="iOS" src="https://img.shields.io/badge/iOS-12%20%26%2014%2B-lightgrey">
  <img alt="Chromium" src="https://img.shields.io/badge/Chromium-M149-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-Experimental-orange">
  <img alt="License" src="https://img.shields.io/badge/license-GPL--3.0-blue">
</p>

<p align="center">
  <strong>Experimental browser.</strong> Expect bugs and crashes.
</p>

## About

Blinker Fluid is an experimental privacy-focused browser that ports Chromium's **Blink** rendering engine and **V8** JavaScript engine to iOS, allowing websites to run without relying on Apple's built-in **WebKit** engine.

The project primarily targets jailbroken and TrollStore-capable devices, bringing a Chromium-based browser to older iOS versions where the bundled version of WebKit may struggle with some modern websites.

## Why?

I started Blinker Fluid because **Ungoogled Chromium** is my primary desktop browser (not counting Tor), and I wanted to see if Chromium's Blink engine could run on jailbroken iOS.

Another reason was that many modern websites no longer work correctly with older versions of WebKit bundled with older iOS releases, which many jailbroken users are unable or unwilling to update from.

## Requirements

### Recommended

- arm64e device
- iOS 15.4, iOS 17.2.1, or iOS 12.5.7
- TrollStore or a jailbreak

These configurations have been personally tested.

### Compatibility

Blinker Fluid should theoretically work on iOS 11 and iOS 14, but these versions have not yet been personally tested.

Blinker Fluid may also work on other iOS versions through [LiveContainer](https://github.com/LiveContainer/LiveContainer). The JIT build may also be usable with tools such as StikDebug.

For iOS 5-10 devices, I would recommend [Venetium-iOS](https://github.com/Computershik73/Venetium-iOS). Venetium is another Chromium port for iOS meant for iOS 10 all the way down to iOS 5. It's still a very early project, though it looks promising. Venetium is NOT maintained by me, it is maintained by [Ilya Vysotsky](https://github.com/Computershik73) so do not report any Venetium issues here, this is the wrong place for that.

Not every LiveContainer configuration has been personally tested, so results may vary.

| Device | iOS version | Status |
| --- | --- | --- |
| iPhone 13 Pro | iOS 15.4 | ✅ |
| iPhone 14 Pro Max | iOS 17.2.1 | ✅ |
| iPhone 6+ | iOS 12.5.7 | ✅ |
| iPad 7th Generation | iOS 17.5.1 | ✅ |
| Unknown Device | iOS 15.2 | ✅ |
| iPhone 12 Pro Max| iOS 14.1 | ✅ |
| Unknown Device | iOS 16.0.2 | ✅ |
| iPad Air 1 | iOS 12.5.8 | ✅ |
| iPhone 11 Pro Max | iOS 14.2 | ✅ |
| iPhone Air | iOS 26.0.1 — Sideloaded + Developer certificate| ✅ |
| iPhone 11 | iOS 26.2 — [LiveContainer](https://github.com/LiveContainer/LiveContainer) | ✅ |
| Unknown Device | iOS 26.1 — [LiveContainer](https://github.com/LiveContainer/LiveContainer) | ✅ |

If you successfully test Blinker Fluid on another iOS version or device, **please open an issue so compatibility can be documented**.

## Features

- Chromium Blink rendering engine
- V8 JavaScript engine
- Modern website compatibility
- Tab manager
- Bookmarks
- Browsing history
- Multiple search engines
- Desktop & mobile browsing
- Video playback
- Face ID / Passcode app lock
- Private Mode
- Built-in content/ad blocking
- Optional SOCKS5 / Tor proxy support
- Dark mode support

## Installation

### TrollStore

1. Download the latest IPA from [**Releases/Tags**](https://github.com/Nodesclock/Blinker-Fluid/tags).
2. Import it into TrollStore.
3. Tap **Install**.
4. Launch Blinker Fluid.

### Other signing tools

Other signing methods such as ESign or GBox may work, but they have not been officially tested.

## JIT Compilation

Blinker Fluid is available in both **JITless** and **JIT** builds.

The JIT version is now more stable, though if you encounter issues, consider trying the JITless build.

JITless builds may feel slower and can have issues loading certain websites because V8 cannot use its normal JIT compilation path.

## Screenshots

*Screenshots from an iPhone 13 Pro running iOS 15.4.*

| ChatGPT | Reddit | Blinker Fluid | Gemini | GitHub |
| --- | --- | --- | --- | --- |
| <img width="250" alt="ChatGPT" src="https://github.com/user-attachments/assets/4fcb4b9e-35bc-4ede-82d0-6a39943929ff" /> | <img width="250" alt="Reddit" src="https://github.com/user-attachments/assets/49b20585-2736-419c-930c-07d7e30628ae" /> | <img width="250" alt="Blinker Fluid" src="https://github.com/user-attachments/assets/c015af7f-712d-40da-af6f-8c1f116ad841" /> | <img width="250" alt="Gemini" src="https://github.com/user-attachments/assets/58090529-1e27-417c-a740-9aa77c63a6c2" /> | <img width="250" alt="GitHub" src="https://github.com/user-attachments/assets/2138d0d2-086c-4833-85f3-70634b96dec3" /> |

## What is being worked on or may be added in the future

- [x] Better iOS version compatibility  
  iOS 12 support was added in Blinker Fluid v.0.3.1.

- [x] JIT support  
  Officially supported since v.0.2.1 and continuing to receive stability and performance improvements.

- [x] Built-in ad/content blocker

- [ ] Website compatibility improvements  
  Continuously being improved with each release.

- [ ] Further Private Mode / browsing privacy improvements

## Features that will most likely never be added

- [ ] Extension support  
  Implementing full Chromium extension support on iOS would be extremely complex and time-consuming, so it is not currently planned.

- [ ] Built-in password manager  
  This would also require significant additional work. Use iCloud Keychain, [Aurora](https://github.com/Luki120/AuroraC), or another password manager instead.

- [ ] Reader mode

> [!IMPORTANT]
> AI was used as an assistant during the creation of Blinker Fluid. It was used to assist with development in these areas:
>
> - Research on porting Blink and V8 to iOS.
> - Assisting with some parts of development.
> - Helping me diagnose and fix smaller bugs.
> - Helping me with translating things to English. (Apologies if README sounds AI generated.)

## Source Code

Yes! Blinker Fluid is fully open source. Contributions and pull requests are accepted and greatly appreciated as long as the fix for the issue that is being addressed was fully tested and confirmed to be a valid fix.

The Chromium source overlay and main build configuration are available directly in this repository.

Blinker Fluid is based on Chromium **M149** at a pinned Chromium revision. The repository does not contain the entire Chromium source tree; instead, the `src/` directory contains the files modified by Blinker Fluid and is intended to be applied over a normal Chromium checkout.

## Building Omivayka Browser for TrollStore

The Omivayka Browser JIT package is built from the pinned Chromium overlay
below. It updates the installed JIT build under its existing bundle identifier.

### Requirements

- A Mac with **Xcode 16.2** (the releases are built with the iOS 18.2 SDK).
- An **iOS Simulator runtime** installed in Xcode (Xcode → Settings → Components). The main build compiles an asset catalog with `actool`, which refuses to run without a simulator runtime, even for a device build.
- [depot_tools](https://chromium.googlesource.com/chromium/tools/depot_tools.git) on your `PATH`.
- [`ldid`](https://github.com/ProcursusTeam/ldid) on your `PATH` (for example `brew install ldid`).
- About **120 GB** of free disk space. The first build takes several hours.

Run the commands from the extracted Blinker Fluid source folder (the folder that contains `src/` and `build_args.gn`). Builds and packages are created in a separate work folder; existing downloaded IPAs are not changed.

### 1. Download Chromium and apply the source overlay

```sh
export SRC="$PWD"
export BLINKER_WORK="$(mktemp -d "$HOME/blinker-build.XXXXXX")"
cd "$BLINKER_WORK"

gclient config --spec='solutions = [{"name": "src", "url": "https://chromium.googlesource.com/chromium/src.git", "managed": False, "custom_deps": {}, "custom_vars": {}}]; target_os = ["ios"]; target_os_only = True'
gclient sync --nohooks --revision src@31dce68b925c2b8efc93df832a86a7c0d03e3fa2

rsync -a "$SRC/src/" src/
cd src
gclient runhooks
```

`BASE_COMMIT.txt` lists the Chromium and V8 revisions the overlay is made for. `gclient sync` checks out the matching V8 automatically.

### 2. Select one package family

**Main release (iOS 14 and later):**

```sh
OUT=blink15
MIN_OS=14.0
BUNDLE_ID=com.nodesclock.blinkerfluid
mkdir -p "out/$OUT"
cp "$SRC/build_args.gn" "out/$OUT/args.gn"
```

**Legacy release (iOS 12 and later), the download named `iOS.12.11`:**

```sh
OUT=blink12
MIN_OS=12.0
BUNDLE_ID=com.nodesclock.blinkerfluid.ios12
mkdir -p "out/$OUT"
cat > "out/$OUT/args.gn" <<'EOF'
target_os = "ios"
target_cpu = "arm64"
target_environment = "device"
use_blink = true
is_debug = false
is_component_build = false
ios_enable_code_signing = false
symbol_level = 0
mac_sdk_min = "14.5"
ios_deployment_target = "12.0"
ios_content_shell_bundle_identifier = "com.nodesclock.blinkerfluid.ios12"
treat_warnings_as_errors = false
v8_enable_sandbox = false
v8_enable_pointer_compression = false
v8_enable_drumbrake = false
cppgc_enable_caged_heap = false
proprietary_codecs = true
ffmpeg_branding = "Chrome"
dcheck_always_on = false
content_shell_version = "149.0.7821.0"
content_shell_major_version = "149"
blinker_legacy_ios_address_space = true
blinker_enable_diagnostics = false
EOF
```

> [!NOTE]
> Despite its download filename, the current legacy package targets iOS 12.0 and later, not iOS 11. It turns off V8 pointer compression and shrinks PartitionAlloc's address-space reservations, because 1 GB devices cannot reserve the address space the main build uses.

### 3. Build

```sh
gn gen "out/$OUT"
autoninja -C "out/$OUT" -j 2 content_shell
```

Wait for each command to finish successfully. Build one family at a time. `-j 2` keeps memory use low; raise it if your Mac has plenty of RAM.

### 4. Package the JIT update

Use the original package for the JIT build installed on the target device (or
its app's `Info.plist`). Build the matching family above. The installed
identifier, minimum iOS version and build metadata are checked before packaging.

```sh
python3 "$SRC/src/tools/blinker/package_omivayka_jit.py" \
  "$BLINKER_WORK/src/out/$OUT/content_shell.app" \
  "/path/to/installed-blinker-jit.tipa" \
  "$BLINKER_WORK/packages/$OUT"
shasum -a 256 "$BLINKER_WORK/packages/$OUT/"*.tipa
```

The packager copies the app into a staging directory, installs the Omivayka
icon, signs the staged bundle with the project entitlements and writes one
versioned `.tipa`. The original package and build output are kept for rollback.
If the installed build already has an equal or newer version, raise both
version fields in `src/content/shell/app/ios/ios-app.plist` before rebuilding.

Add `--standalone` to package a separate installation with bundle identifier
`com.wingto.omivayka.jit` and its own app data.

Back up the installed browser's data before testing the update in TrollStore.
Check that ordinary tabs, bookmarks and settings survive, then launch with
TrollStore's **Open with JIT** and verify the runtime tier on the target device.
A diagnostic build with `blinker_enable_diagnostics = true` reports
`JIT_AUTH` and `JIT_TIER`; ordinary release builds keep diagnostics off.

> [!NOTE]
> The original Blinker Fluid artwork in `src/content/shell/app/ios/resources/artwork` is drawn by [@Waguriii_draws](https://www.instagram.com/waguriii_draws/) and is probably not covered by the GPL license. The Omivayka icon was generated separately.

## Credits

- [Reynard Browser](https://github.com/minh-ton/reynard-browser) by [Minh Ton](https://github.com/minh-ton) for heavily inspiring the creation of Blinker Fluid.
- [TrollStore](https://github.com/opa334/TrollStore) by [opa334](https://github.com/opa334) and all contributors.
- [Chromium](https://github.com/chromium/chromium) for being most of Blinker Fluid.
- [Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium) for heavily inspiring the creation of Blinker Fluid too.
- [EasyList and EasyPrivacy](https://easylist.to) by the EasyList creators, used as the built-in ad and tracker blocking lists.
- [@Waguriii_draws](https://www.instagram.com/waguriii_draws/) on Instagram for creating the Blinker Fluid app icons and all Blinker Fluid art. Great friend and an amazing artist!
