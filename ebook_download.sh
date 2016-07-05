#!/bin/sh

Name="mitosis" #write the name of the book here
python download_ebook.py

mkdir $Name
cd $Name

mv ../file.txt $Name.txt
ebook-convert $Name.txt $Name.epub #change the file extension to the format you wish. .mobi for mobi files
