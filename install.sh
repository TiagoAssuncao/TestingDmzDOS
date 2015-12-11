sudo apt-get -f install
sudo apt-get upgrade
sudo apt-get update
cd loic/
sudo apt-get install git-core monodevelop
./loic.sh install
./loic.sh update
cd ..
sudo apt-get install hping3
sudo apt-get install ostinato
git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
