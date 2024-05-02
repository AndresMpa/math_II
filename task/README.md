### Usage

Create a virtual environment using python:

```bash
python -m venv env
source ./env/bin/activate
pip install -r ./requirements.txt
```

Then create a .env file, and copy-paste the following configuration

```bash
MODE="8"

IMAGE_SIZE=200
IMAGE_DIR="images"
MATRIX_DIR="matrix"

MATRIX_MAX=1000
MATRIX_MIN=1

SAVE_IMAGE_DIR="img_result"
SAVE_MATRIX_DIR="mtx_result"

WEB_SITE="https://picsum.photos"

VERBOSE=0
AUTOCLEAR=0
```

##### Configuration

Your .env file can control each section of the code, this is pretty simple

| Options           | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| `MODE`            | Testing mode from `./test_sets/`, 1 to 4 means vectors while 5 to 8 means matrix                |
| `IMAGE_SIZE`      | It means the size XxY of defaults images donwloaded from [lorem picsum](https://picsum.photos/) |
| `IMAGE_DIR`       | You can configure a directory to donwload images                                                |
| `MATRIX_DIR`      | If you want to load an image you can do it using this option (CSV only)                         |
| `MATRIX_MAX`      | Matrices defaults use random matrix this option defines the _max possible_ number for it        |
| `MATRIX_MIN`      | Matrices defaults use random matrix this option defines the _min possible_ number for it        |
| `SAVE_IMAGE_DIR`  | From test 1 to 4 some image will be created so you must specify the directory                   |
| `SAVE_MATRIX_DIR` | From test 5 to 8 some csv files will be created so you must specify the directory               |
| `WEB_SITE`        | [lorem picsum](https://picsum.photos/) is the default provider, but you can define another      |
| `VERBOSE`         | This option enable a full feature log using a terminal (Use 1 to enable it)                     |
| `AUTOCLEAR`       | To remove file before starting a new run you can enable this option (Use 1 to enable it)        |
