import zipfile

def extract_first_20k_from_zip(zip_path, out_src_path, out_tgt_path, src_file="EuroPat.de-en.en", tgt_file="EuroPat.de-en.de", max_lines=20000):
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(src_file) as src_f, z.open(tgt_file) as tgt_f:
            with open(out_src_path, 'w', encoding='utf-8') as out_src, \
                 open(out_tgt_path, 'w', encoding='utf-8') as out_tgt:

                for i, (src_line, tgt_line) in enumerate(zip(src_f, tgt_f)):
                    if i >= max_lines:
                        break
                    out_src.write(src_line.decode('utf-8'))
                    out_tgt.write(tgt_line.decode('utf-8'))

    print(max_lines)
    print(out_src_path)
    print(out_tgt_path)


if __name__ == "__main__":
    extract_first_20k_from_zip(
        zip_path="EuroPat.de-en.txt.zip",
        out_src_path="EuroPat.de-en.20k.en",
        out_tgt_path="EuroPat.de-en.20k.de"
    )