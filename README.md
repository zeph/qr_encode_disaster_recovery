# qr_encode_disaster_recovery
paranoid mode, give mommy a copy of your backup encryption keys (printed)

well, we had to split the key in 3 to fit the 1000-something character to have a bit of error control

and you need to export/ascii armor your key when you get it out of gnupg

 1. `$ kubectl get secret -n kube-system sealed-secrets-key -o yaml | yq.v2 r - data[tls.key]|base64 -d > tls.key`
 2. `$ cat ../tls.key| python create_printouts.py`
 	1. `$ virtualenv -p python3 .p3`
	2. `$ source .p3/bin/activate`
	3. `(.p3)$ pip install -r requirements.txt`
 3. `$ convert chunk0.svg chunk1.svg chunk2.svg  -page a4 -resize 150% chunk.pdf`

[...] // disaster occurring

 1. `(.p3)$ python verify_camera.py`
 2. `ctrl+C` (to exit, with focus/mouse pointer on the shell) or `<space>` to read again
