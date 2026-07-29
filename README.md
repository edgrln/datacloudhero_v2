rm -rf output
pelican content -o output -s pelicanconf.py

rm -rf output
pelican content -o output -s publishconf.py


pelican -l --bind 0.0.0.0