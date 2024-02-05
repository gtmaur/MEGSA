## MEGSA Event QR Code Generator ##




Welcome to the MEGSA Event QR Code Generator! This Python script, `Src_QR_Code_Generator.py`, enables you to effortlessly create visually appealing QR codes for MEGSA events. The generated QR code, seamlessly blended with a background image, will be saved as a PNG file on your Desktop.



### Installation ###
#### 1. Clone the repository
```
git clone https://github.com/MEGSA-AME/MEGSA.git
cd MEGSA/Src
```

#### 2. Setting up all the requiremnts libraries
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using::
```
pip install -r requirements.txt
```

To changes the folders where your logo files are located make modifications; additionally give a better event name and associated url:
```
event_name=Name of the MEGSA event
megsa_image_or_logo_path=Path to the background image
url_to_encode=The URL you want to encode in the QR code

```


#### 3. Run the code

```
python python Src_QR_Code_Generator.py.py
```


Please cite the following paper if this model helps your research:

	@inproceedings{deng2019accurate,
	    title={Accurate 3D Face Reconstruction with Weakly-Supervised Learning: From Single Image to Image Set},
	    author={Yu Deng and Jiaolong Yang and Sicheng Xu and Dong Chen and Yunde Jia and Xin Tong},
	    booktitle={IEEE Computer Vision and Pattern Recognition Workshops},
	    year={2019}
	}
##
The face images on this page are from the public [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) dataset released by MMLab, CUHK.