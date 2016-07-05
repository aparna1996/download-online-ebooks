# download-online-ebooks
You can convert like http://www.bestlib4u.com, http://www.freevampires.net etc into ebooks for a comfortable offline reading.

Open the .py file and replace the url with the URL you want to download

Run the Script with
$ ./ebook_download.sh

This will create a folder with the text file of the download and the modified epub file.

OPTIONS:
-If you want to change the name of the file, open the script and change the name in the first line there
-If you want to change the format of the file, replace .epub with the format of your choice.

PREREQUISITES:
-Make sure you have python3 installed
-To install the required python libraries type
pip3 install BeautifulSoup4, request, re
