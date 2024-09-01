#
# Title: driver.py
# Description: 
#
import sys
import uuid

import yaml
from yaml.loader import SafeLoader

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from postgres import PostGres
from sql_table import Fortune

class Driver:

    def __init__(self, postgres:PostGres):
        self.postgres = postgres

    def file_reader(self, file_name: str) -> list[str]:
        buffer = []

        try:
            with open(file_name, "r", encoding="utf-8") as infile:
                buffer = infile.readlines()
                if len(buffer) < 1:
                    print(f"empty file noted: {file_name}")
        except:
            print(f"file read error: {file_name}")

        return buffer

    def free_bsd_loader(self, buffer: list[str]) -> None:
        temp = "".join(buffer)
#        print(f"{len(buffer[0])} {len(buffer)}, {temp}")
        self.postgres.fortune_insert(str(uuid.uuid4()), temp)
    
    def free_bsd_extractor(self, raw_file:str) -> None:
        raw_buffer = self.file_reader(raw_file)
        temp_buffer = []

        for ndx in range(len(raw_buffer)):
            if raw_buffer[ndx].startswith("%") and len(raw_buffer[ndx]) == 2:
                self.free_bsd_loader(temp_buffer)
                temp_buffer.clear()
            else:
                temp_buffer.append(raw_buffer[ndx])

        self.free_bsd_loader(temp_buffer)

    def plan9_extractor(self, raw_file:str) -> None:
        raw_buffer = self.file_reader(raw_file)

        for ndx in range(len(raw_buffer)):
            #print(raw_buffer[ndx])
            self.postgres.fortune_insert(str(uuid.uuid4()), raw_buffer[ndx])

    def execute(self, raw_file:str) -> None:
        print("execute")

        if "freebsd" in raw_file:
            self.free_bsd_extractor(raw_file)
        elif "plan9" in raw_file:
            self.plan9_extractor(raw_file)

        return

if __name__ == '__main__':
    print("main")

    if len(sys.argv) > 1:
        config_file_name = sys.argv[1]
    else:
        config_file_name = "config.yaml"

    configuration = None

    try:
        with open(config_file_name, "r", encoding="utf-8") as stream:
            configuration = yaml.load(stream, Loader=SafeLoader)
    except yaml.YAMLError as error:
        print(error)

    if len(configuration) < 1:
        print("empty configuration noted")
        sys.exit(1)

    db_engine = create_engine(configuration['db_conn'], echo=False)
    postgres = PostGres(sessionmaker(bind=db_engine, expire_on_commit=False))

    driver = Driver(postgres)
    driver.execute(configuration['raw_file'])

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
