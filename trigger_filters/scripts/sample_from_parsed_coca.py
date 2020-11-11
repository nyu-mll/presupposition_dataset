import argparse, os
import random

def main():
    parser = argparse.ArgumentParser(description='Dependency parse individual COCA file with spacy.')
    parser.add_argument('--parsed_path', help='Path to directory containing parsed COCA files')
    parser.add_argument("--output_path", default="..", help="Output path for parsed files")
    parser.add_argument("--proportion_sentences", type=float, help='Total number of sentences to select.')
    args = parser.parse_args()

    n_sentences = 0
    out_file = open(args.output_path, "w")

    for genre in os.listdir(args.parsed_path):
        if not os.path.isdir(os.path.join(args.parsed_path, genre)):
            continue
        for file in os.listdir(os.path.join(args.parsed_path, genre)):
            if not file.endswith(".conll"):
                continue
            in_file = open(os.path.join(args.parsed_path, genre, file), encoding="utf-8")
            try:
                while True:
                    n_sentences += 1
                    chunk = ""
                    line = next(in_file)
                    while line != "\n":
                        chunk += line
                        line = next(in_file)
                    if random.uniform(0, 1) < args.proportion_sentences:
                        chunk = chunk.split("\n")
                        chunk.insert(1, f"# genre = {genre}")
                        chunk.insert(2, f"# file = {file}")
                        chunk = "\n".join(chunk)
                        out_file.write(chunk + "\n")
            except StopIteration:
                continue
    print(n_sentences)
    out_file.close()


if __name__ == '__main__':
    main()
