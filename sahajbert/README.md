
# What is this experiment about?
This experiment is a project by the paper authors in which we aim to train an ALBERT model for Bengali collaboratively.

# Training ALBERT with decentralized averaging

## Preparation 
* Install the library (`src`) from the root folder
* Dependencies: `pip install -r requirements.txt`
* Preprocess data following the instructions in `tokenizer_training` folder
* Upload the archive with preprocessed data to somewhere your peers can reach


## Running an experiment
- Run the first DHT peer to welcome trainers and record training statistics (e.g. loss, performance):
   - In this example, we use [wandb.ai](https://wandb.ai/site) to plot training metrics; If you're unfamiliar with Weights & Biases, here's a [quickstart tutorial](https://docs.wandb.ai/quickstart).
   - Run `python run_first_peer.py --listen_on '[::]:*' --experiment_prefix NAME_YOUR_EXPERIMENT --wandb_project WANDB_PROJECT_HERE`
   - `NAME_YOUR_EXPERIMENT` must be a unique name of this training run, e.g. `Bengali-albert`. It cannot contain `.` due to naming conventions.
   - `WANDB_PROJECT_HERE` is a name of wandb project used to track training metrics. Multiple experiments can have the same project name.
   - This peer will run a DHT node on a certain IP/port (`Running DHT root at ...`). You will need this address for next steps


- To join the collaboration as a participant, it's enough to run the `contributor_notebook.ipynb`.


# Evaluation

We use scripts to evaluate on downstream tasks, based on the original finetuning scripts from the transformers repository.

Datasets:
- NER: "wikiann", "bn"
- NCC: "indic_glue", "sna.bn"

Models:
- sahajBERT (place a trained model in any suitable location)
- "xlm-roberta-large"
- "ai4bharat/indic-bert"
- "neuralspace-reverie/indic-transformers-bn-roberta"


Required arguments:
```shell
--model_name_or_path
--output_dir
```

## Examples

### NER

```shell
python train_ner.py \
  --model_name_or_path xlm-roberta-large \
  --output_dir sahajbert/ner \
  --learning_rate 1e-5 \
  --max_seq_length 128 \
  --num_train_epochs 20 \
  --per_device_train_batch_size 128 \
  --per_device_eval_batch_size 128 \
  --early_stopping_patience 3 \
  --early_stopping_threshold 0.01
```

### NCC

```shell
python train_ncc.py \
  --model_name_or_path xlm-roberta-large \
  --output_dir sahajbert/ncc \
  --learning_rate 1e-5 \
  --max_seq_length 128 \
  --num_train_epochs 20 \
  --per_device_train_batch_size 128 \
  --per_device_eval_batch_size 128 \
  --early_stopping_patience 3 \
  --early_stopping_threshold 0.01
```
