# ParTy2OPUS

ParTy2OPUS converts documents from the [ParTy corpus](http://www.natalialevshina.com/corpus.html) to the [OPUS](http://opus.nlpl.eu/) format, to allow easier processing in other applications dealing with parallel corpora.

## Installation

ParTy2OPUS requires the following to be installed/downloaded:

* The [ParTy corpus](https://github.com/levshina/ParTy-1.0).
* [Uplug](https://bitbucket.org/tiedemann/uplug/wiki/Home). Uplug comes with [hunalign](https://github.com/danielvarga/hunalign) installed.
* [TreeTagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/). ParTy2OPUS expects TreeTagger to be installed in `/opt/treetagger/`.

## Details 

The OPUS format is XML-based, while ParTy is text-based.
Since there is already quite some tooling available for parallel corpora in OPUS, we created a Python script which converts the ParTy corpus into the OPUS format.
We allow users to pick their preferred languages and also allow to add part-of-speech tagging and lemmatization.
We redo the original sentence alignment using hunalign.
The resulting corpus can then be queried using, for example, the [PerfectExtractor](https://github.com/UUDigitalHumanitieslab/perfectextractor/) package.

## Example usage

    # Setting up the corpus environment
    cd ~/Documents
    git clone git@github.com:levshina/ParTy-1.0.git
    mkdir ParTyOPUS
    
    # Setting up this package
    git clone git@github.com:time-in-translation/ParTy2OPUS.git
    cd ParTyOPUS
    pip install -r requirements.txt
    
    # Running the extraction for German, English, Spanish, Dutch, and French
    # and also running part-of-speech tagging. 
    python process.py ~/Documents/ParTy-1.0/ ~/Documents/ParTyOPUS/ de en es nl fr --tag
