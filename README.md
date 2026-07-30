rm -rf output
pelican content -o output -s pelicanconf.py

rm -rf output
pelican content -o output -s publishconf.py





make devserver
