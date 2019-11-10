while getopts "12345" opt; do
		
  cartereseau=$(ls /sys/class/net | grep enp)
  case ${opt} in
    1 )
        echo "MAC ADDRESS : 3c:d9:2b:68:82:8f"
        macaddress="3c:d9:2b:68:82:8f"
      ;;

    2 )
        echo "MAC ADDRESS : 3c:d9:2b:68:88:e8"
        macadress="3c:d9:2b:68:88:e8"
      ;;

    3 )
        echo "MAC ADDRESS : 3c:d9:2b:68:45:69"
        macaddress="3c:d9:2b:68:45:69"
      ;;

    4 )
		echo "Re-initialize services"
		unset http_proxy
		unset HTTP_PROXY
		unset ftp_proxy
		unset FTP_PROXY
		unset all_proxy
		unset ALL_PROXY
		unset https_proxy
		unset HTTPS_PROXY
		sudo ip link set dev $cartereseau down
		sudo ip link set dev $cartereseau up
		sudo service network-manager restart
		echo "Goodbye my friend!"
		break
      ;;

    5 )
      ;;
    \? ) echo "Goodbye my friend!"
		break
      ;;
  esac
	sudo ip link set dev $cartereseau down
	sudo ip link set dev $cartereseau address $macaddress
	sudo ip link set dev $cartereseau up
	#sudo ip address add 172.20.12.220/24 dev enp4s0
	export http_proxy=http://192.168.1.16:8080/
	export HTTP_PROXY=http://192.168.1.16:8080/
	export ftp_proxy=http://192.168.1.16:8080/
	export FTP_PROXY=http://192.168.1.16:8080/
	export all_proxy=http://192.168.1.16:8080/
	export ALL_PROXY=http://192.168.1.16:8080/
	export https_proxy=http://192.168.1.16:8080/
	export HTTPS_PROXY=http://192.168.1.16:8080/


	echo "You've been linked to the ENSTA Bretagne!"
done