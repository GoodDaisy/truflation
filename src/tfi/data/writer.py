"""
Writer
"""

from tfi.data.bundle import Bundle, BundleFormat
import pandas
import sqlalchemy
from sqlalchemy import Table, MetaData, create_engine


class Writer:
    def __init__(self):
        pass

    def write_all(
            self,
            inputb: Bundle,
            *args, **kwargs
    ):
        for i in self.write_chunk(
                inputb
        ):
            pass

    def write_chunk(
            self,
            inputb: Bundle,
            *args, **kwargs
    ):
        raise NotImplementedError

class WriterSql(Writer):
    def __init__(self, engine):
        super(Writer, self).__init__()
        self.engine = create_engine(engine)

    def write_all(
            self,
            inputb: Bundle,
            *args,
            **kwargs
    ):
        inputb.get(BundleFormat.PANDAS).to_sql(
            kwargs['table'],
            self.engine
        )

    def write_chunk(
            self,
            inputb: Bundle,
            *args, **kwargs
    ):
        self.write_all(inputb, *args, **kwargs)


    def drop_table(
            self,
            table_name: str,
            ignore_fail: bool = True
    ):
        try:
            tbl = Table(
                table_name, MetaData(),
                autoload_with=self.engine
            )
        except sqlalchemy.exc.NoSuchTableError:
            if ignore_fail:
                return
            else:
                raise
        tbl.drop(self.engine, checkfirst=False)

class WriterCSV(Writer):
    def __init__(self):
        super(Writer, self).__init__()

    def write_all(
            self,
            data: Bundle,
            *args, **kwargs) -> None:
        data.get(BundleFormat.PANDAS).to_csv(args[0])