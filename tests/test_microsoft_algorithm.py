from selection.algorithms.microsoft_algorithm import MicrosoftAlgorithm
from selection.workload import Workload
from selection.index import Index
from mock_connector import MockConnector, mock_cache, column_A_0, column_A_1, column_A_2, query_1, query_2, table_A

import unittest
import logging

# logging.basicConfig(
#     filename=
#     '/Users/wieso/Documents/phd/research/index_selection_evaluation/example3.log',
#     level=logging.DEBUG)


class TestMicrosoftAlgorithm(unittest.TestCase):
    def setUp(self):
        self.connector = MockConnector()
        self.database_name = 'test_DB'

    def test_calcualte_indexes_2indexes_3columns(self):
        algorithm = MicrosoftAlgorithm(database_connector=self.connector,
                                       parameters={
                                           "max_indexes": 2,
                                           "max_index_columns": 3
                                       })
        algorithm.cost_evaluation.cache = mock_cache
        algorithm.cost_evaluation._prepare_cost_calculation = lambda indexes, store_size=False: None

        indexes = algorithm.calculate_best_indexes(
            Workload([query_1, query_2], self.database_name))
        self.assertEqual(set(indexes),
                         set([Index([column_A_0, column_A_1, column_A_2])]))

    def test_calcualte_indexes_2indexes_2columns(self):
        algorithm = MicrosoftAlgorithm(database_connector=self.connector,
                                       parameters={
                                           "max_indexes": 2,
                                           "max_index_columns": 2
                                       })
        algorithm.cost_evaluation.cache = mock_cache
        algorithm.cost_evaluation._prepare_cost_calculation = lambda indexes, store_size=False: None

        indexes = algorithm.calculate_best_indexes(
            Workload([query_1, query_2], self.database_name))
        self.assertEqual(set(indexes), set([Index([column_A_0, column_A_1])]))


if __name__ == '__main__':
    unittest.main()