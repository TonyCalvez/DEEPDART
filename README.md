# DEEPDART 

## JETSON TX2 - DEVELOPER KIT

### INSTALLATION JETPACK 3.3

#### SDK Manager Software

![](IMG/screensdkmanager.png)

#### SDK Manager : Not supported on ubuntu1904

To support the NVIDIA Software, you need to change the environment variable in the directory : `/etc/` 

WARNING : You need to save et restore at the end of this tips the files: `os-release` and `lsb-release`.

Configuration File : 

File : `os-release`

```txt
NAME="Ubuntu"
VERSION="18.04 (Disco Dingo)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=disco
UBUNTU_CODENAME=disco
```

File : `lsb-release`

```txt
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04 LTS"
```







### INSTALLATION DES BIBLIOTHEQUES POUR LE GGPU TEGRA X2 

Download link : https://developer.nvidia.com/embedded/downloads#/search=tensorflow

#### TensorFlow for JetPack : 

Documentations : https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html

