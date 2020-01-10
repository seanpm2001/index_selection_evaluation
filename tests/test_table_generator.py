from selection.table_generator import TableGenerator
from selection.dbms.postgres_dbms import PostgresDatabaseConnector
import unittest


class TestTableGenerator(unittest.TestCase):
    def setUp(self):
        self.db_connector = PostgresDatabaseConnector(None,
                                                      autocommit=True)

    def test_generate_tpch(self):
        table_generator = TableGenerator('tpch', 0.001, self.db_connector)
        self.assertEqual(table_generator.database_name(),
                         'indexselection_tpch___0_001')

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            TableGenerator('not_tpch', 0.001, self.db_connector)

    def test_tpcds_with_wrong_sf(self):
        with self.assertRaises(Exception):
            TableGenerator('tpcds', 0.002, self.db_connector)


if __name__ == '__main__':
    unittest.main()