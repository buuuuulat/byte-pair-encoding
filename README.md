# Byte Pair Encoding

Hi 👋🏻 this is an implementation of the BPE algorithm from scratch. This repo
includes code I originally wrote as part of an assignment for Stanford's CS336 course.

---

## OpenWebText train run result
It took ~6 hours to train BPE on MacBook Pro (M3 Pro, 18 GB of unified memory)
with vocab size of 32000.

### Sample from merges:
```text
( lat<=|=>itude)
( fet<=|=>ish)
( F<=|=>ruit)
(iv<=|=>ists)
(D<=|=>isp)
```

### Sample from vocab:
```json
{
  "31995": " latitude",
  "31996": " fetish",
  "31997": " Fruit",
  "31998": "ivists",
  "31999": "Disp"
}
```


## How to run
1. `uv sync`

2.  Download TinyStories and OpenWebText:
    ```bash
    mkdir -p data
    cd data
    
    wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-train.txt
    wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt
    
    wget https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_train.txt.gz
    gunzip owt_train.txt.gz
    wget https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_valid.txt.gz
    gunzip owt_valid.txt.gz
    
    cd ..
    ```
3. Set training parameters in the `if __name__ == "__main__:` section of [train_bpe.py](byte_pair_encoding/train_bpe.py)
4. Run it: `uv run ./byte_pair_encoding/train_bpe.py`
5. Results will be saved to `./outputs/` folder.
