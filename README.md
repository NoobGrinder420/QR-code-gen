# PyQR
Creates a QR code from the terminal.

## Prerequisites
Make sure you have the following libraries installed:

```bash
$ pip install pillow
$ pip install qrcode
```
How to Use
Run the following command to generate a QR code:

```bash
$ python3 path/to/main.py parameters
```
Parameters
Assumes that main.py is in your working directory.

-name: Input the name of the QR code file.

Example:
```bash
$ python3 main.py -name "sigma"
```
This will store your QR code filename as sigma_qr.png.

Default value: sample (filename will be sample_qr.png).
-url: Input the URL for the QR code.

Example:
```bash
$ python3 main.py -name "sigma" -url "https://www.youtube.com/"
```
This will generate a QR code that links to YouTube.

Default value: "https://www.youtube.com/".
-path: Input the path where you want to store the QR code file.

Example:
```bash
$ python3 main.py -path "./qr-codes/"
```
This will store your QR code in a new/existing folder called qr-codes in your current working directory.

Default value: "./" (your current working directory).
