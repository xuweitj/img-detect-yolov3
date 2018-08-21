cd ./darknet/scripts/
mkdir -p VOCdevkit
cd VOCdevkit
mkdir -p VOC2007
cd VOC2007

# copy all the images and labels
echo "copy images and labels from source"
mkdir -p Annotations ImageSets JPEGImages labels
cp ../../../../../data/labelled/all_data/xml/* ./Annotations/
cp ../../../../../data/labelled/all_data/image/* ./JPEGImages/

# get train and test filenames
cd ImageSets
mkdir -p Main
cd Main
ls ../../../../../../../data/labelled/train_data/image/ | cut -d "." -f1 > train.txt
ls ../../../../../../../data/labelled/test_data/image/ | cut -d "." -f1 > test.txt

# convert image and label format
cd ../../../../
echo "converting image format to jpeg"
sh convert_image_format.sh
echo "converting label format"
python voc_label.py
