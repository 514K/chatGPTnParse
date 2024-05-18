# Rewrite sites with chatGPT

## Get started
Before start set prompt in `prompt.txt`

Usage as:
```
python main.py <api_key> <dir_with_txt>
python new_to_cur.py
```

## Results

### main.py
Before:
/<dir_with_txt>
-- <file_name1>.txt
-- <file_name2>.txt
...
-- <file_nameN>.txt

After:
/<dir_with_txt>
-- <file_name1>.txt
-- <file_name1>-new.txt
-- <file_name2>.txt
-- <file_name2>-new.txt
...
-- <file_nameN>-new.txt


### new_to_cur.py
Remove all `<source_name>-new.txt` files to `<source_name>.txt`
Use this after checking all texts. 