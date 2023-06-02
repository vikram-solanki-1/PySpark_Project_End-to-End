### Check if SSH is installed
ssh

### Generate the provate and public key using ssh-keygen
ssh-keygen

### Copy the content of public key to authorized key file.
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

### Test ssh localhost
ssh localhost

###Validate by exit
exit
