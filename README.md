# image2music_2.0

Image2music_2.0 allows you to compose music just by selecting a source image file. The program processes the image and creates a musical piece of configurable length. 

## Example
For example, using this image as a source file:

![Tourists Image](/tourists.jpg)

an approximatley 5 second long [piece of music](https://www.dropbox.com/s/2p9y2qy7afz5j9m/tourists.wav?dl=0) was created.


## Usage
### Dependencies
- [Python Imaging Library (PIL)] (http://www.pythonware.com/products/pil/)
- [PySynth](https://mdoege.github.io/PySynth/)

### Creating music from images
```
cd image2music_2.0
python image2music.py [source image] [output audio].wav [output length seconds]
```

The example above was created with the following:
```
python image2music.py tourists.jpg tourists.wav 5
```
