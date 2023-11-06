# crop-all-photos


```
git clone https://github.com/highlightime/crop-all-photos.git
```

1. Put your photos like screenshot to input image folder

2. Enjoy functions make images to pdfs or pptx, crop image, merge pdfs to one pdf


```
python3 main.py -h
usage: main.py [-h] {crop,pdf,merge,pptx} ...

Programs that can crop many images at once or make them into PDFs and PPTs

optional arguments:
  -h, --help            show this help message and exit

subcommand:
  {crop,pdf,merge,pptx}
    crop                Function to crop images
    pdf                 Function to convert images to PDF
    merge               Function to merge PDF files
    pptx                Function to convert images to PPTX
```

For example, 
`python3 main.py pptx input_images out.pptx`
`python3 main.py pdf input_images pdfs_dir`
`python3 main.py merge pdfs_dir out.pdf`
`python3 main.py crop input_images cropped_images 0 110 1530 980`


