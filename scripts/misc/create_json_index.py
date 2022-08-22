# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Create json index from metadata files.

This file is used primarily to allow remote fetching of Security Datasets
metadata with minimal latency.

It creates the following sets of files:
/data/.index/sec-dsets-index.json
/data/.index/sec-dsets-index.json.zip
/data/.index/sec-dsets-index.json.gz

"""
import argparse
import json
import gzip
import zipfile
from pathlib import Path
from typing import Any, Dict, Literal, Union, get_args

import yaml

_SD_DATA = "datasets"
_SD_FOLDERS = ["atomic", "compound"]
_MD_FOLDER = "_metadata"
_DEF_INDEX_NAME = "sec-dsets-index"
_DEF_OUT_FOLDER = ".index"

OutputType = Literal["all", "json", "gz", "zip"]


def main(
    input_dir: Union[str, Path],
    target_dir: Union[str, Path],
    output: OutputType,
    verify: bool = False,
):
    """
    Consolidates yaml metadata files and writes json output.

    Parameters
    ----------
    input_dir : Union[str, Path]_
        Path to root of input data files.
    target_dir : Union[str, Path]
        Path to save output files.
    output : OutputType
        The format(s) to write the output files.
    verify : bool
        If True, verify the written files contain the same content
        as the parsed yaml files.

    """
    index_dict = _metadata_to_dict(input_dir)
    print("Metadata files read:")
    print(f"{len(index_dict)} folders")
    print(sum(len(fldr) for fldr in index_dict.values()), "files")
    print(f"output to {target_dir}")
    _write_index_files(index_dict, target_dir, output)

    if verify:
        _verify_files(index_dict=index_dict, target_dir=target_dir, output=output)


def _read_metadata(source_dir: Union[str, Path]) -> Dict[str, Any]:
    """Read folder of metadata yamls and returns dictionary."""
    return {
        str(Path(file).stem): yaml.safe_load(Path(file).read_text(encoding="utf-8"))
        for file in Path(source_dir).joinpath(_MD_FOLDER).glob("*.yaml")
    }


def _metadata_to_dict(source_dir) -> Dict[str, Any]:
    """Return consolidated dictionary of input folders."""
    return {
        folder: _read_metadata(Path(source_dir).joinpath(folder))
        for folder in _SD_FOLDERS
    }


def _write_index_files(
    index_dict: Dict[str, Any], target_dir: Union[str, Path], output: OutputType
):
    """
    Write index file outputs.

    Parameters
    ----------
    index_dict : Dict[str, Any]
        File metadata dictionary.
    target_dir : Union[str, Path]
        Output folder.
    output : OutputType
        Output file types to write.

    """
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    json_index_path = target_dir.joinpath(_DEF_INDEX_NAME).with_suffix(".json")
    index_json = json.dumps(index_dict)

    print("Output format", output)
    if output in ("all", "json"):
        json_index_path.write_text(index_json, encoding="utf-8")
        print(f"created JSON index: {json_index_path}")
    if output in ("all", "zip"):
        with zipfile.ZipFile(
            f"{json_index_path}.zip", "w", compression=zipfile.ZIP_BZIP2
        ) as f_zip:
            f_zip.writestr(json_index_path.name, data=bytes(index_json, encoding="utf-8"))
        print(f"created zip index: {json_index_path}.zip")
    if output in ("all", "gz"):
        with gzip.open(f"{json_index_path}.gz", "wb") as f_gzip:
            f_gzip.write(bytes(index_json, encoding="utf-8"))
        print(f"created gz index: {json_index_path}.gz")


def _verify_files(
    index_dict: Dict[str, Any], target_dir: Union[str, Path], output: OutputType
):
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    json_index_path = target_dir.joinpath(_DEF_INDEX_NAME).with_suffix(".json")

    if output in ("all", "json"):
        index_json = json_index_path.read_text(encoding="utf-8")
        json_dict = json.loads(index_json)
        if index_dict == json_dict:
            print(f"Verified JSON index: {json_index_path}")
        else:
            print(f"ERROR: JSON index is different: {json_index_path}")

    if output in ("all", "zip"):
        with zipfile.ZipFile(f"{json_index_path}.zip", "r") as f_zip:
            with f_zip.open(json_index_path.name, "r") as f_zip_file:
                content = f_zip_file.read()
                zip_dict = json.loads(content.decode(encoding="utf-8"))
        if index_dict == zip_dict:
            print(f"Verified ZIP index: {json_index_path}.zip")
        else:
            print(f"ERROR: ZIP index is different: {json_index_path}.zip")

    if output in ("all", "gz"):
        content = bytes(index_json, encoding="utf-8")
        with gzip.open(f"{json_index_path}.gz", "rb") as f_gzip:
            content = f_gzip.read()
            gz_dict = json.loads(content.decode(encoding="utf-8"))
        if index_dict == gz_dict:
            print(f"Verified GZ index: {json_index_path}.gz")
        else:
            print(f"ERROR: GZ index is different: {json_index_path}.gz")


def _add_script_args():
    parser = argparse.ArgumentParser(description="Security datasets index generator")

    parser.add_argument(
        "--output-path",
        "-o",
        default=f"./{_SD_DATA}/{_DEF_OUT_FOLDER}",
        required=False,
        help="Path to output folder.",
    )

    parser.add_argument(
        "--input-path",
        "-i",
        default=f"./{_SD_DATA}",
        required=False,
        help="Path to input folder holding atomic and compound datasets.",
    )

    parser.add_argument(
        "--formats",
        "-f",
        default="all",
        choices=get_args(OutputType),
        required=False,
        help="The type of output file(s) to create for the index.",
    )
    parser.add_argument(
        "--verify",
        "-v",
        action="store_true",
        help="Verify file(s) after writing.",
    )
    return parser


if __name__ == "__main__":
    arg_parser = _add_script_args()
    args = arg_parser.parse_args()

    main(
        target_dir=args.output_path,
        input_dir=args.input_path,
        output=args.formats,
        verify=args.verify,
    )
