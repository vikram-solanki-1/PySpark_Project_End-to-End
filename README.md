# PySpark_Project_End-to-End Project
* Project FLow Diagram
<img width="666" alt="ProjectFlowDiagram" src="https://github.com/solanki1750/PySpark_Project_End-to-End/assets/134689573/19bb005a-a344-46ae-bc07-31aa0ac2bf78">

* Data Ingestion Flow
<img width="710" alt="data ingestion" src="https://github.com/solanki1750/PySpark_Project_End-to-End/assets/134689573/e16a46ac-9855-4bf2-afe3-41cf438b52d9">

* Business requirement
<img width="588" alt="business requireemnt" src="https://github.com/solanki1750/PySpark_Project_End-to-End/assets/134689573/85b29c1d-2ad6-46e6-8336-e72b2658543d">

* Process Flow
<img width="685" alt="processflow" src="https://github.com/solanki1750/PySpark_Project_End-to-End/assets/134689573/a4f32fc6-8c77-4157-bf6f-8b2e061534ca">

* GCP, HDFS, Hadoop, Yarn setup


Created VM Instance, created static ip, open SSH in browser, on Terminal - $ python3 (pythos is already installed), it does not have all modules so we may need to import required modules. $ exit(). $ sudo apt update -> update existing list of packages. now, install pip. $sudo apt install python3-pip. now install venv for python. $ sudo apt install python3-vene. $ python3 -m vene tutorial-env. now we need to install java $ sudo apt-get install openjdk-8-jdk. Now check if its installed by $ java -version. $ javac -version

* Password less login on single node
check if ssh installed $ ssh $ ls -lrt $ cd .ssh (nothing is present there). let go back to previous directory $ cd now create a NO(blank) password file. $ ssh-keygen and enter with no inputs. $ cd .ssh (now in ssh directory) $ ls -lrt (we see two files id_rsa.pub which is a public file and id_rsa which is private file). Now we need to copy the content of publick file into authorise key file (this key file specify ssh keys that can be used for login into localhost). Copy the content of public key to authorized key file.
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys now, Test ssh localhost $ ssh localhost

* Setup Hadoop tar, hdfs, yarn
Download hadoop tar (Latest as of today). $ wget https://mirrors.gigenet.com/apache/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz   $ ls -lrt. Untar the File.
$ tar xfz hadoop-3.3.1.tar.gz    Set up folder structure. $ sudo mv -f hadoop-3.3.1 /opt $ sudo chown ${USER}:${USER} -R /opt/hadoop-3.3.1       Create a softlink as /opt/hadoop.
$ sudo ln -s /opt/hadoop-3.3.1 /opt/hadoop         Update below three lines in the .profile file.
-- export HADOOP_HOME=/opt/hadoop
-- export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin 
-- export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64 
