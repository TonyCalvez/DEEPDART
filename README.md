# DEEPDART 

## JETSON TX2 - DEVELOPER KIT

### INSTALLATION JETPACK 3.3

#### SDK Manager Software :

![](IMG/screensdkmanager.png)

You need to follow this different step to install :

- The Operating System : JetPack (last release) with the Ubuntu Linux Kernel with an architecture for AARCH64.

  - Flashing the OS with USB cable and the Recovery Mode :
    - Plug the USB cable from the host to the micro-USB
    - Plug the power cable
    - Start the Jetson Developer Kit with the button POWERBIN and click on the button REC simultaneously during 2 secs

- The programs and libraries on the host (Error : unavailable for my Linux 19.04)

- The programs and libraries on the Jetson TX2 

  

#### SDK Manager : Not supported on ubuntu1904 :

To support the NVIDIA Software, you need to change the environment variable in the directory : `/etc/` 

**WARNING** : You need to save now et restore it at the end of this files: `os-release` and `lsb-release`.

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

Restart your software !



### LIBRARIES POUR LE GGPU TEGRA X2 

Download link : https://developer.nvidia.com/embedded/downloads#/search=tensorflow

#### TensorFlow for JetPack : 

Documentations : https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html

**Installation :** 

Download package : [tf_gpu-1.14.0+nv19.7-py3](https://developer.download.nvidia.com/compute/redist/jp/v42/tensorflow-gpu/tensorflow_gpu-1.14.0+nv19.7-cp36-cp36m-linux_aarch64.whl)





