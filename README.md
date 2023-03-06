# sysrepo_tester
cd /root<br />
git clone https://github.com/xscchoux/sysrepo_tester.git<br />
cd sysrepo_tester<br />
docker build -t test_sysrepo -f /root/test_sysrepo/base.Dockerfile .<br/>
docker run -it sysrepo_tester<br/>


<b>inside the container:</b><br/>
python3 install_yang.py<br/>
python3 delete_yang.py
