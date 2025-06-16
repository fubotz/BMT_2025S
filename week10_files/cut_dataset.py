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


# if __name__ == "__main__":
#     extract_first_20k_from_zip(
#         zip_path="EuroPat.de-en.txt.zip",
#         out_src_path="EuroPat.de-en.20k.en",
#         out_tgt_path="EuroPat.de-en.20k.de"
#     )


def extract_range_from_zip(zip_path, src_file, out_path, start_line, end_line):
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(src_file) as src_f:
            with open(out_path, 'w', encoding='utf-8') as out_f:
                for i, line in enumerate(src_f):
                    if i >= end_line:
                        break
                    if i >= start_line:
                        out_f.write(line.decode('utf-8'))

    print(f"Extracted {start_line} to {end_line-1} to {out_path}")

if __name__ == "__main__":
    extract_range_from_zip(
        zip_path="EuroPat.de-en.txt.zip",
        src_file="EuroPat.de-en.en",
        out_path="EuroPat.de-en.test.en",
        start_line=20000,
        end_line=20050
    )