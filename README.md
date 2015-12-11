<h1>Teste DOS DMZ</h1>
Aglomerado de ferramentas DOS utilizadas para testar a eficiência da aplicação DMZ.

<h2>Instalando Ferramentas</h2>
Neste pacote contém várias ferramentas, várias já estão preparadas para uso, outras, fazem necessário a sua instalação. Para instalar, rode o comando:
<br>

sh install.sh
<br>
<h2>Utilizando Ferramentas</h2>
Segue a utilização das ferramentas.

<h3>Hping3</h3>
A hping3 será utilizada para testar a aplicação TCP SYN. Para iniciá-la, o comando deve ser:
 <br>
 hping3 --flood --syn --rand-source -c 10000 -p 80 ipDeDestino
<br>
<h3>Utilizando g3m</h3>
g3m Para ataque udp na porta 2081. COMANDO:  
<br>
./g3m -U -h 192.168.40.15 -p 2081,2081

<h3>Loic</h3>
Loic para testar aplicações HTTP.
utilizar o ./loic run 

<h3>Utilização do SQLMap</h3>
O sqlmap é escrito em python2.7. Para iniciá-lo:
<br>
python sqlmap.py -h

